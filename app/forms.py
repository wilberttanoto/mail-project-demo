from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired
from datetime import datetime

class MailForm(FlaskForm):
	"""
	Form to add or edit the mail form
	"""
	email = StringField('Email', validators=[DataRequired()])
	email_body = TextAreaField('Email Body', validators=[DataRequired()])
	email_subject = StringField('Email Subject', validators=[DataRequired()])
	timestamp = DateTimeField("Time Stamp",
                          format="%Y-%m-%d %H:%M:%S", 
                          default=datetime.today,
                          validators=[DataRequired()])
