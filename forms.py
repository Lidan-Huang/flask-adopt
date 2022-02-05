"""Forms for adopt app."""
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
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
                               ('senior', 'Senior')]) #TODO validators
    notes = StringField("Notes") #TODO validators


class EditPetForm(FlaskForm):
    """Form to edit pet details"""
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    notes = StringField("Notes") #TODO validators  
    available = BooleanField('Available')                     
