from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('db:27017')
db = client.ContactDB

app = Flask(__name__)


@app.route("/add_contact", methods=['POST'])
def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = db.Contacts.insert_one({
                "name" : user_name,
                "contact" : user_contact
            })
        return dumps({'message' : 'SUCCESS'})
    except :
        return dumps({'error' : 'test'})


@app.route("/get_all_contact", methods = ['GET'])
def get_all_contact():
    try:
        contacts = db.Contacts.find()
        return dumps(contacts)
    except:
        return dumps({'error': 'test'})

@app.route('/')
def hello_world():
    return 'Server is Up!!!'
