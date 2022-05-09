from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddPitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [DataRequired()])
    pitch = StringField("Go", validators = [DataRequired()])
    category = SelectField(
        "category",
        choices=[("pick-ups", "pick-ups"),("boring","boring")],validators = [DataRequired()]
    )
    submit = SubmitField("Add pitch")