from . import auth
from .forms import RegistrationForm,LoginForm
from . import auth
from app.models import User
from .forms import RegistrationForm,LoginForm
from flask import render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user
# from app.email import create_mail

@auth.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    
    title = 'Utmost Pitches- Register'
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        pass_input = form.password.data
        profile_pic = "photos/default.png"
        bio = "User has no bio"
        new_user = User(name = name, email = email, password = pass_input,profile_pic = profile_pic, bio = bio)
        new_user.save_user()
        # create_mail("Hey Karibu","email/email",new_user.email,name = new_user.name)


    return render_template("auth/register.html",form = form, title = title)


@auth.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()

    title = 'Utmost Pitches- Register'
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        remember = form.remember_me.data

        user = User.query.filter_by(email = user_email).first()

        # if user is not None and user.verify_password(form.password.data):
        #     login_user(user,form.remember.data)
        #     return redirect(request.args.get('next') or url_for('main.index'))

        if user is not None and user.verify_password(user_password):
            login_user(user,remember)
            flash("Karibu!! This is Utmost Pitches")
            return render_template("main.index", user = user)
            
            flash("Invalid username or pasword")
    return render_template("auth/login.html",form = form, title = title)    


auth.route("/logout")
def logout():
    logout_user()

    flash("Hey! You have logged out Successfully")
    return redirect(url_for("main.index"))    