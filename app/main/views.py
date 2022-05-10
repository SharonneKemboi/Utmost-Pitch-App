from flask import abort, flash, render_template,redirect,url_for,request
from ..models import User,Pitch,Comment
from .forms import AddPitchForm,AddComment,EditBio
from . import main
from flask_login import login_required
import datetime
from ..import photos,db



@main.route("/")
def index():
    pitches = Pitch.query.all()
    title = "Home"
    return render_template("index.html", pitches = pitches, title=title)

@main.route("/pitches/<category>")
def categories(category):
    pitches = None
    if category == "all":
        pitches = Pitch.query.all()
    else:
        pitches = Pitch.query.filter_by(category = category).all()

    return render_template("pitches.html", pitches = pitches, title = category.upper())



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

        return redirect(url_for("main.categories",category = category))

    return render_template("add_pitch.html", form = form, title = title) 


@main.route("/<user>/pitch/<pitch_id>/add/comment", methods = ["GET","POST"])
@login_required
def comment(user,pitch_id):
    user = User.query.filter_by(id = user).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = AddComment()

    title = "Add comment"
    if form.validate_on_submit():
        content = form.content.data
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]

        new_comment = Comment(content = content, user = user, pitch = pitch, time = time, date = date, title = title )
        new_comment.save_comment()
        flash(f"Comment for {pitch.title.upper()} added")

        return redirect(url_for("main.view_comments", pitch_id = pitch_id))
    return render_template("comment.html", title = pitch.title,form = form)

@main.route("/<pitch_id>/comments")
@login_required
def view_comments(pitch_id):

     

    pitch = Pitch.query.filter_by(id = pitch_id).first()
    title = "Comments"
    comments = pitch.get_pitch_comments()

    return render_template("view.comments", comments = comments, pitch = pitch,title = title)


@main.route("/profile/<user_id>")
@login_required
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    user_pitches = user.pitches
    if user_pitches:
        pitches = user_pitches
    else:
        pitches = False
    title = user.name.upper()
    return render_template("profile.html", pitches = pitches, user = user, title = title)

@main.route("/pic/<user_id>/update", methods = ["POST"])
@login_required
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()
    title = "Edit Profile"
    if "profile-pic" in request.files:
        pic = photos.save(request.files["profile-pic"])
        file_path = f"photos/{pic}"
        user.profile_pic = file_path
        db.session.commit()
    return redirect(url_for("main.profile", user_id = user.id))


@main.route("/<user_id>/profile/edit",methods = ["GET","POST"])
@login_required
def update_profile(user_id):

    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    form = EditBio()

    if form.validate_on_submit():
        bio = form.bio.data
        user.bio = bio
        db.session.commit() 
        return redirect(url_for('main.profile',user_id = user.id)) 
    return render_template("update_profile.html",form = form, title=title)