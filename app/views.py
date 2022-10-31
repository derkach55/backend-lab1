from app import app
from flask import request, jsonify
from app import USERS, CATEGORY, RECORD


@app.post('/category/')
def create_category():
    category = {
        'id': CATEGORY[-1]['id'] + 1,
        'name': request.get_json()['name']
    }
    CATEGORY.append(category)
    return category


@app.get('/categories/')
def get_categories():
    return jsonify(CATEGORY)
