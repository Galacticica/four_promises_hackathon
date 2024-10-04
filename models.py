'''
File Name: app.py
Authors: Reagan Zierke and Aleksa Chambers
Date: 10/03/24
Description:
This file creates models for questions, responses, users, and sessions. 
'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import csv
import uuid
import os

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







class User(UserMixin):

    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email
        self.password_hash = None
    
    def save(self):
        self.id = get_last_id('users.csv') + 1
        data = [{'id': self.id, 'name': self.name, 'email': self.email, 'pwdigest': self.password_hash}]
        with open('users.csv', mode='a', newline='') as file:
            fieldnames = ['id', 'name', 'email', 'pwdigest']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writerows(data)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @classmethod
    def load(cls, email):
        with open('users.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                print(row)
                if row['email'] == email:
                    user = User(row['name'], row['email'])
                    user.set_password(row['pwdigest'])
                    return user
            return None



class Session:
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.id = None
    
    def save(self):
        self.id = uuid.uuid4()
        data = [{'sessionid' : self.id, 'email' : self.user_id}]
        with open('sessions.csv', mode='a', newline='') as file:
            fieldnames = ['sessionid', 'email']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            # if os.path.getsize(file) == 1:
            #     file.write('\n')
            csv_writer.writerows(data)

    @classmethod
    def load(cls, session_id):
        with open('sessions.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['sessionid'] == session_id:
                    return cls(row.user_id)