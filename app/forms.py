from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class LatLong(FlaskForm):
    start = StringField('Home Zip Code', validators=[DataRequired()])
    end = StringField('Current Zip Code', validators=[DataRequired()])
    price = StringField('Price Range', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Favorites(FlaskForm):
    submit = SubmitField('Submit')