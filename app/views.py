#  This file contains all the routes for our application. This will tell Flask what to display on which path

from flask import render_template,request,redirect,url_for,flash

from app import app, db

from models import MailMail

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
	add_email = True
	if request.method == 'POST':
		email = request.form['email']
		email_subject = request.form['email_subject']

		email = MailMail(email=email,email_subject=email_subject)
		try:
			db.session.add(email)
			db.session.commit()
			flash('You have successfully added a new email.')
		except:
			flash('Something went wrong with the email.')
		return redirect(url_for('list_emails'))
	else:
		return render_template("add_email.html", add_email=add_email)


@app.route('/save_emails/edit/<int:id>', methods=['GET', 'POST'])
def edit_email(id):
	"""
		Edit emails
	"""
	mail = MailMail.query.get_or_404(id)
	if request.method == 'POST':
		mail.email = request.form.get('email', None)
		mail.email_subject = request.form.get('email_subject', None)

		db.session.add(mail)
		db.session.commit()
		flash('You have successfully editted an email.')
		return redirect(url_for('list_emails'))
	else:
		return render_template("edit_email.html", email=mail.email,email_subject=mail.email_subject)

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
	
