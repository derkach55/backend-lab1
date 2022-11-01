from app import app
from flask import request, abort
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


@app.post('/records/')
def create_record():
    if request.method == 'POST':
        try:
            record = {
                'id': RECORD[-1]['id'] + 1,
                'user_id': request.get_json()['user_id'],
                'category_id': request.get_json()['category_id'],
                'payment': request.get_json()['payment']
            }
        except KeyError:
            return abort(400)
        RECORD.append(record)
        return record


@app.get('/records/<int:user_id>/')
def get_records_by_user(user_id):
    records = list(filter(lambda x: x['user_id'] == user_id, RECORD))
    return records if records else abort(404)


@app.get('/records/<int:user_id>/<int:category_id>/')
def get_records_by_user_and_category(user_id, category_id):
    records = list(filter(lambda x: x['user_id'] == user_id and x['category_id'] == category_id, RECORD))
    return records if records else abort(404)
