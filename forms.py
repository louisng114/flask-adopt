from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, RadioField
from wtforms.validators import AnyOf, URL, NumberRange, optional

class NewPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name: ")
    species = StringField("Species: ", validators=[AnyOf(values=["cat", "dog", "porcupine"], message="We only accept cat, dogs, and porcupines")])
    photo_url = StringField("Photo URL: ", validators=[URL(message="Please provide a valid URL"), optional()])
    age = IntegerField("Age: ", validators=[NumberRange(min=0, max=30, message="Age must be from 0 to 30"), optional()])
    notes = StringField("Notes: ")

class PetEditForm(FlaskForm):
    """Form for editing pet info"""

    photo_url = StringField("Photo URL: ", validators=[URL(message="Please provide a valid URL"), optional()])
    age = IntegerField("Age: ", validators=[NumberRange(min=0, max=30, message="Age must be from 0 to 30"), optional()])
    notes = StringField("Notes: ")
    available = BooleanField("Available: ")
