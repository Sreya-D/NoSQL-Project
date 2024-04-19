from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] = "cd69f3e3e159dd8171e0f6c40a293f08d0c22ec3"
app.config["MONGO_URI"] = "mongodb+srv://sreya:Sreya1234@flasktodo.bv3srbj.mongodb.net/"

mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes