'''
File Name: database_reader.py
Authors: Reagan Zierke and Aleksa Chambers
Date: 10/01/24
Description:
This file is used to write and read questions and responses to their respective CSV files. 
It creates functions that can be accessed from the app.py file in order to get the neccesary data for the HTML code.
'''
import csv




def get_last_id(filename):
    '''
    This gets the last id of the database passed.

    Parameters
    ----------
    filename : string
        Name of the file to get the id from

    Returns
    -------
    int
        The ID of the last item in the passed database
    '''
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        if len(rows) > 0:
            return int(rows[-1]['id'])
        else:
            return 0



def write_question(question):
    '''
    Writes the question asked by the user to the questions.csv database.

    Parameters
    ----------
    question : string
        The question asked by the user
    '''
    last_id = get_last_id('questions.csv')
    data = [{'id': last_id+1, 'question': question, 'userid': 'N/A'}]
    with open('questions.csv', mode='a', newline='') as file:
        fieldnames = ['id', 'question', 'userid']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        if last_id == 0:
            file.write('\n')
        csv_writer.writerows(data)

def read_questions():
    '''
    This function reads all the questions and returns them to be used on the webpage.

    Returns
    -------
    List of dictionaries
        Returns all the questions, along with their id and the user who wrote the question
    '''
    all_questions = []
    with open('questions.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            all_questions.append(row)
    return all_questions

def read_specific_question(question_id):
    '''
    This function returns a specific question based on the question ID.

    Parameters
    ----------
    question_id : int
        The ID of the question to be returned

    Returns
    -------
    row[question] string
        The specific question based on the questionid

    row[userid] string
        The id of the user who wrote the question based on questionid
    '''
    with open('questions.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['id'] == question_id:
                return row['question'], row['userid']
            




def write_response(response, questionid):
    '''
    Writes the response entered by the user to the responses.csv database.

    Parameters
    ----------
    response : string
        The response the user entered to the question
    questionid : int
        The ID of the question being responded to
    '''
    last_id = get_last_id('responses.csv')
    data = [{'id': last_id+1, 'response': response, 'questionid': questionid, 'userid': 'N/A'}]
    with open('responses.csv', mode='a', newline='') as file:
        fieldnames = ['id', 'response', 'questionid', 'userid']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        if last_id == 0:
            file.write('\n')
        csv_writer.writerows(data)

def read_responses(questionid):
    '''
    This function collects all the responses for the question passed in and returns them and their user.

    Parameters
    ----------
    questionid : int
        The ID of the question to get repsonses for

    Returns
    -------
    List of dictionaries
        All the responses for the question corresponding to the questionid passed in.
    '''
    question_responses = []
    with open('responses.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['questionid'] == questionid:
                question_responses.append(row)
    return question_responses