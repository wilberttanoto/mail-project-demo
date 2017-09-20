from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class MailForm(FlaskForm):
	"""
	Form to add or edit the mail form
	"""
	email = StringField('Email', validators=[DataRequired()])
	email_body = TextAreaField('Email Body', validators=[DataRequired()])
	email_subject = StringField('Email Subject', validators=[DataRequired()])
