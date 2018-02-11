from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField
from wtforms.validators import DataRequired

class LatLong(FlaskForm):
    lat = DecimalField('Latitude', validators=[DataRequired()])
    long = DecimalField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Submit')