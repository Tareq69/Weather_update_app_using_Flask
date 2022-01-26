from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Searchform(FlaskForm):
    location = StringField(label='City Name',validators=[DataRequired()])
    submit = SubmitField(label="Search for your city")