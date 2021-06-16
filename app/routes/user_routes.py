from flask import Blueprint, jsonify, current_app
from ..controllers import user_controller
from ..bot.auth import auth

current_app.config['CORS_HEADERS'] = 'Content-Type'
bp_users = Blueprint('users', __name__)


@bp_users.route('/auth', methods=['POST'])
def authenticate():
    return auth()

@bp_users.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Hello Wold'})

@bp_users.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_users()


@bp_users.route('/users/<uid>', methods=['GET'])
def get_user(uid):
    return user_controller.get_user(uid)


@bp_users.route('/users', methods=['POST'])
def post_user():
    return user_controller.post_user()


@bp_users.route('/users/<uid>', methods=['DELETE'])
def delete_users(uid):
    return user_controller.delete_user(uid)


@bp_users.route('/users/<uid>', methods=['PUT'])
def update_users(uid):
    return user_controller.update_user(uid)