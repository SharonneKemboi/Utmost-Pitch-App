from flask import abort, flash, render_template,redirect,url_for,request
from ..models import User,Pitch,Comment
from .forms import AddPitchForm,AddComment
from . import main
from flask_login import login_required
import datetime
from ..import photos,db



@main.route("/")
def index():
    pitches = Pitch.query.all()
    title = "Home"
    return render_template("index.html", pitches = pitches)

@main.route("/pitches/<category>")
def categories(category):
    pitches = None
    if category == "all":
        pitches = Pitch.query.all()
    else:
        pitches = Pitch.query.filter_by(category = category).all()

    return render_template("pitches.html", pitches = pitches, title = category)



@main.route("/<uname>/add/pitch", methods = ["GET","POST"])
@login_required
def add_pitch(uname):
    form = AddPitchForm()
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)
    title = "Create Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]

        new_pitch = Pitch(title = title, content = pitch, category = category,user = user,date =date, time = time)
        new_pitch.save_pitch()
        pitches = Pitch.query.all()

        return redirect(url_for("main.index"))

    return render_template("add_pitch.html", form = form, title = title) 


@main.route("/<user>/pitch/<pitch_id>/add/comment", methods = ["GET","POST"])
@login_required
def comment(user,pitch_id):
    user = User.query.filter_by(id = user).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = AddComment()

    if form.validate_on_submit():
        content = form.content.data
        new_comment = Comment(content = content, user = user, pitch = pitch )
        new_comment.save_comment()
        flash(f"Comment for {pitch.title.upper()} added")
        return redirect(url_for("main.categories", category=pitch.category))
    return render_template("comment.html", title = pitch.title,form = form)

@main.route("/<pitch_id>/comments")
@login_required
def view_comments(pitch_id):

    pitch = Pitch.query.filter_by(id = pitch_id).first()

    comments = pitch.get_pitch_comments()

    return render_template("view.comments", comments = comments, pitch = pitch)


@main.route("/profile/<user_id>")
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    pitches = user.pitches

    return render_template("profile.html", pitches = pitches, user = user)

@main.route("/pic/<user_id>/update", methods = ["POST"])
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()

    if "profile-pic" in request.files:
        pic = photos.save(request.files["profile-pic"])
        file_path = f"photos/{pic}"
        user.profile_pic = file_path
        db.session.commit()
    return redirect(url_for("main.profile", user_id = user.id))

