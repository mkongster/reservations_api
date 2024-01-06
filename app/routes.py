from flask import jsonify, request

from app import app, reservations
from app.database import db
from app.models import User


@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/users', methods=['GET'])
def get_users():
    #db.create_all()
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], type='provider', id=1)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/submit_availability', methods=['PUT'])
def submit_availability():
    data = request.get_json()
    result = reservations.submit_availability(data['provider_id'], data['appointments'])
    return jsonify(result)

@app.route('/reserve', methods=['POST'])
def reserve():
    #TODO:
    pass

@app.route('/confirm', methods=['POST'])
def confirm():
    #TODO:
    pass

@app.route('/get_available_appointments', methods=['GET'])
def get_available_appointments():
    #TODO:
    pass