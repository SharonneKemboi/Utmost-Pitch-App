from flask import render_template
from ..models import User,Pitch,Comment
from .forms import AddPitchForm
from . import main

@main.route("/")
def index():
    form = AddPitchForm()
    title = "Create Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        new_pitch = Pitch(title = title, content = pitch, category = category)
        new_pitch.save_pitch()

    return render_template("index.html", form = form, title = title) 