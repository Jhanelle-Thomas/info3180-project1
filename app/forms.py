from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField
from wtforms.validators import InputRequired

class profileForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    gender = SelectField(label='Gender', choices=[("Female", "Female"), ("Male", "Male")])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    