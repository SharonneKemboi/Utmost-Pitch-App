from . import auth
from .forms import RegistrationForm
from app.models import User
from flask import render_template

@auth.route("/", methods = ["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        pass_input = form.password.data

        new_user = User(name = name, email = email, password = pass_input)
        new_user.save_user()
    return render_template("auth/login.html",form = form)