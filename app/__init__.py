from flask import Flask
from app.data import USERS, CATEGORY, RECORD

app = Flask(__name__)

from app import views
