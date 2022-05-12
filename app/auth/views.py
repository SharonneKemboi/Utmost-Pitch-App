from flask import render_template,url_for,redirect,flash,request
from . import auth
from .forms import RegistrationForm,LoginForm
from ..import db
from app.models import User
from flask_login import login_user,logout_user,login_required
# from app.email import create_mail

@auth.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        profile_pic = "photos/default.png"
        bio = "User has no bio"
        new_user = User(name = username, email = email, password = password,profile_pic = profile_pic, bio = bio)
        # new_user.save_user()
        db.session.add(new_user)
        db.session.commit()
        # create_mail("Hey Karibu","email/email",new_user.email,name = new_user.name)
        return redirect(url_for('auth.login'))
    title = 'Utmost Pitches- Register'
    return render_template("auth/register.html",form = form, title = title)
    #Return redirect


@auth.route("/login", methods = ["GET","POST"])
def login():
    login_form= LoginForm()

    
    if login_form.validate_on_submit():
        # user_email = login_form.email.data
        # user_password = login_form.password.data
        # remember = login_form.remember_me.data
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember_me)
            flash("Karibu!! This is Utmost Pitches")
            return redirect(request.args.get('next') or url_for('main.index'))
           
        flash("Invalid username or pasword")
    title = 'Utmost Pitches- Login'
    return render_template("auth/login.html",login_form = login_form, title = title)    



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))