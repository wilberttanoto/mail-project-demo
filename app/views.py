#  This file contains all the routes for our application. This will tell Flask what to display on which path

from flask import render_template,request,redirect,url_for,flash

from app import app, db
from .forms import MailForm

from models import MailMail

from datetime import datetime

@app.route('/')
@app.route('/save_emails', methods=['GET', 'POST'])
def list_emails():
	"""
		Listing all emails
	"""
 	emails = MailMail.query.all()
	return render_template("list_emails.html", emails=emails)


@app.route('/save_emails/add', methods=['GET', 'POST'])
def add_email():
	"""
		Add emails
	"""
	form = MailForm()
	add_email = True

	if request.method == 'POST' and form.validate_on_submit():
		email = form.email.data
		email_subject = form.email_subject.data
		email_body = form.email_body.data
		# timestamp = datetime.strptime(form.timestamp.data,'%Y-%m-%d %H:%M:%S')
		timestamp = form.timestamp.data

		email = MailMail(email=email,email_subject=email_subject,email_body=email_body,timestamp=timestamp)
		try:
			db.session.add(email)
			db.session.commit()
			flash('You have successfully added a new email.')
		except:
			raise
			flash('Something went wrong with the email.')
		return redirect(url_for('list_emails'))
	else:
		return render_template("add_email.html", form=form, add_email=add_email)


@app.route('/save_emails/edit/<int:id>', methods=['GET', 'POST'])
def edit_email(id):
	"""
		Edit emails
	"""
	email = MailMail.query.get_or_404(id)
	form = MailForm(obj=email)
	
	if request.method == 'POST' and form.validate_on_submit():
		email.email = form.email.data
		email.email_subject = form.email_subject.data
		email.email_body = form.email_body.data
		email.timestamp = form.timestamp.data
		try:
			db.session.add(email)
			db.session.commit()
			flash('You have successfully editted a new email.')
		except:
			flash('Something went wrong with the email.')
		return redirect(url_for('list_emails'))
	else:
		form.email.data = email.email
		form.email_subject.data = email.email_subject
		form.email_body.data = email.email_body
		form.timestamp.data = email.timestamp
		return render_template("edit_email.html", form=form)

@app.route('/save_emails/delete/<int:id>', methods=['GET', 'POST'])
def delete_mail(id):
	"""
		Delete emails
	"""
	mail = MailMail.query.get_or_404(id)
	db.session.delete(mail)
	db.session.commit()
	flash('You have successfully deleted an email.')
	return redirect(url_for('list_emails'))		
	
