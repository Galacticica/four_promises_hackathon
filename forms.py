'''
File Name: forms.py
Authors: Reagan Zierke and Aleksa Chambers
Date: 10/01/24
Description:
This file creates the forms used to get and post the data entered by the user.
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
#   This creates the form for users to ask questions
    question = StringField('Question', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ResponseForm(FlaskForm):
#   This creates the form for users to respond to questions
    response = StringField('Response', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
#   This creates the form users use to sign up
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LogInForm(FlaskForm):
#   This creates the form to log in with
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class TestForm(FlaskForm):
    text = StringField('Text')
    submit = SubmitField('Submit')