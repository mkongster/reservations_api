from flask import jsonify, request

from app import app
from app.database import db
from app.models import User


@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201
