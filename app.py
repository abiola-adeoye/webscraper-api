import os

from flask import Flask
from flask_restful import Api

from db import db
from dotenv import load_dotenv



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True