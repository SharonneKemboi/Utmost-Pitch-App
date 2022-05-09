from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddPitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [DataRequired()])
    pitch = TextAreaField("Go", validators = [DataRequired()])
    category = SelectField(
        "category",
        choices=[("pick-ups", "pick-ups"),("dull","dull"),("Goofy","Goofy"),("sales","sales"),("mucic","music"),("cheesy","cheesy"),("random","random")],validators = [DataRequired()]
    )
    submit = SubmitField("Add pitch")


class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")    


class EditBio(FlaskForm):
    bio = StringField("Bio")
    submit = SubmitField("Update")     