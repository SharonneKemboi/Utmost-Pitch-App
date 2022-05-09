from . import mail
from flask_mail import Message
from flask import render_template

def create_mail(subject,template,to,**kwargs):

    welcome_message = Message(subject,sender="sharonnekay23@gmail.com",recipients = [to])
    welcome_message.body = render_template(template + ".txt", **kwargs)
    mail.send(welcome_message)