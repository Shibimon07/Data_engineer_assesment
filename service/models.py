
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String)
    address_line1 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    pincode = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    employments = db.relationship('EmploymentInfo', backref='user', cascade='all, delete-orphan', lazy='joined')
    banks = db.relationship('UserBankInfo', backref='user', cascade='all, delete-orphan', lazy='joined')

class EmploymentInfo(db.Model):
    __tablename__ = 'employment_info'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    company_name = db.Column(db.String)
    designation = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_current = db.Column(db.Boolean)

class UserBankInfo(db.Model):
    __tablename__ = 'user_bank_info'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    bank_name = db.Column(db.String)
    account_number = db.Column(db.String)
    ifsc = db.Column(db.String)
    account_type = db.Column(db.String)
