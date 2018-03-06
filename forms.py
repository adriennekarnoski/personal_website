from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()], widget=TextArea())
