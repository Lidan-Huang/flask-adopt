"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form to add a pet."""
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")


