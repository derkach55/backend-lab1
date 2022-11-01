from app import app
from flask import request, jsonify, abort
from app import USERS, CATEGORIES, RECORD


@app.post('/category/')
def create_category():
    try:
        category = {
            'id': CATEGORIES[-1]['id'] + 1,
            'name': request.get_json()['name']
        }
    except KeyError:
        return abort(400)
    CATEGORIES.append(category)
    return category


@app.get('/categories/')
def get_categories():
    return CATEGORIES


@app.post('/user/')
def create_user():
    try:
        user = {
            'id': USERS[-1]['id'] + 1,
            'name': request.get_json()['name']
        }
    except KeyError:
        return abort(400)
    USERS.append(user)
    return user
