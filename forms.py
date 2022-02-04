"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form to add a pet."""
    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                          validators=[InputRequired()],
                          choices=[('cat', 'Cat'),
                                   ('dog', 'Dog'),
                                   ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])

    age = SelectField('Age',
                      choices=[('baby', 'Baby'),
                               ('young', 'Young'),
                               ('adult', 'Adult'),
                               ('senior', 'Senior')])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Edit already showed pet"""
