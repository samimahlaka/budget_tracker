from flask import Flask
from flask_wtf import FlaskForm
from wtforms  import DateField, StringField, FloatField,SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class transactionForm(FlaskForm) :
    date = DateField('date', render_kw={"class":'input_field'}, validators=[DataRequired(message='Date is requred')])
    description=StringField('description',  render_kw={'class':'input_field'},validators=[DataRequired(message='Description is required'), Length(max=100)])
    amount=FloatField('amount', render_kw={'class':'input_field'}, validators=[DataRequired(message='Amount is required'), NumberRange(min=0.01, message="Amount must be positive.")])
    submit = SubmitField('Add Transaction', render_kw={"class": "submit_btn"})

