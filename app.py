'''
File Name: app.py
Authors: Reagan Zierke and Aleksa Chambers
Date: 10/01/24
Description:
This file creates the routing for the website by setting up flask and different app routes. 
'''
from flask import Flask, render_template as rt, redirect, url_for
import forms
import models
import database_reader as qData
from flask_login import LoginManager, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
login = LoginManager(app)

@app.route('/', methods=['GET', 'POST'])
def login_page():
    form = forms.LogInForm()
    if form.validate_on_submit():
        new_user = models.User.load(form.email.data)
        print(new_user.password_hash)
        if new_user is None or not new_user.check_password(form.password.data):
            print(new_user)
            print(new_user.check_password(form.password.data))
            print("There was an error")
            return redirect(url_for('login_page'))
        
        login_user(new_user)
        return redirect(url_for('home_page'))

    return rt("login.html", form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = forms.SignUpForm()

    if form.validate_on_submit():
        new_user = models.User(form.name.data, form.email.data)
        new_user.set_password(form.password.data)
        new_user.save()
        new_session = models.Session(new_user.email)
        new_session.save()
        login_user(new_user)
        return redirect(url_for('home_page'))

    return rt("signup.html", form=form)

@app.route("/home", methods=['GET', 'POST'])
def home_page():
    '''
    This scans for all the questions and creates the home page route

    '''
    questions = qData.read_questions()
    return rt("home.html", questions=questions)


@app.route("/ask-a-question", methods=['GET', 'POST'])
def ask_question_page():
    '''
    This creates a form for users to enter their questions and passes it into the ask a question page, along with creating the ask a question page

    '''
    form = forms.QuestionForm()
    if form.validate_on_submit():
        question = form.question.data
        qData.write_question(question)
        return redirect(url_for('home_page'))
    return rt("ask_question.html", form=form)


@app.route("/question-replies/<questionid>", methods=['GET', 'POST'])
def view_question_page(questionid):
    '''
    This gathers the question that the user clicked on, creates a form for users to enter responses, and creates a page for the question that
    users can respond on

    Parameters
    ----------
    questionid : int
        The id of the question in which the page is for

    '''
    question, userid = qData.read_specific_question(questionid)
    responses = qData.read_responses(questionid)
    form = forms.ResponseForm()
    if form.validate_on_submit():
        response = form.response.data
        qData.write_response(response, questionid)
        return redirect(url_for('view_question_page', questionid=questionid))
    return rt('current_question.html', userid=userid, question=question, responses=responses, form=form)



@login.user_loader
def load_user(id):
    session = models.Session.load(id)
    if session == None:
        return None
    return models.User.load(session.user_id)







