from flask import render_template
from ..models import User,Pitch,Comment
from .forms import AddPitchForm,AddComment
from . import main


@main.route("/<uname>/add/pitch", methods = ["GET","POST"])
def index(uname):
    form = AddPitchForm()
    title = "Create Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user = User.query.filter_by(name = uname).first()
        new_pitch = Pitch(title = title, content = pitch, category = category,user = user)
        new_pitch.save_pitch()
        pitches = Pitch.query.all()

        return render_template("pitched.html", pitches = pitches)

    return render_template("index.html", form = form, title = title) 


@main.route("/<user>/pitch/<pitch_id>/add/comment", methods = ["GET","POST"])
def comment(user,pitch_id):
    user = User.query.filter_by(id = user).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = AddComment()

    if form.validate_on_submit():
        content = form.content.data
        new_comment = Comment(content = content, user = user, pitch = pitch )
        new_comment.save_comment()
    return render_template("comment.html", title = pitch.title,form = form)

@main.route("/<pitch_id>/comments")
def view_comments(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()

    comments = pitch.get_pitch_comments()

    return render_template("view.html", comments = comments)
