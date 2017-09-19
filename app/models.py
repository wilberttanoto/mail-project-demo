from app import db

class MailMail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)