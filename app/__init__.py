from flask import Flask
from app.data import USERS, CATEGORIES, RECORD

app = Flask(__name__)

from app import views
