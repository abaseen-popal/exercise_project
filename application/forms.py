from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ExerciseForm(FlaskForm):
    exercise_name = StringField("Name of exercise: ", validators=[DataRequired()])
    description = StringField("Description of exercise: ", validators=[DataRequired()])
    sets = StringField("Number of sets: ", validators=[DataRequired()])
    reps = StringField("Number of reps: ", validators=[DataRequired()])
    submit =SubmitField("Add Exercise")

class LocationForm(FlaskForm):
    location_name = StringField("Name of location: ", validators=[DataRequired()])
    description = StringField("Description of location: ", validators=[DataRequired()])
    address = StringField("Address: ", validators=[DataRequired()])
    submit =SubmitField("Add Location")

class AddingExerciseLocForm(FlaskForm):
    exercise_name = StringField("Name of exercise: ", validators=[DataRequired()])
    submit =SubmitField("Add Exercise")

class AddingLocToExerciseForm(FlaskForm):
    location_name = StringField("Name of location: ", validators=[DataRequired()])
    submit =SubmitField("Add Location")