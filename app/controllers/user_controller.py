import datetime
from flask import request, jsonify
from ..models.user_model import UserModel
from ..schemas.user_serealize import user_schema, users_schema
from .base_controller import get_all, get_one, delete, post, update
from ..notify.base_notification import is_required
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def get_users():
    logging.info('\033[1;34mGetting all users\033[m')
    return get_all(UserModel, users_schema, 'user')


def get_user(uid):
    logging.info('\033[1;34mGetting one user\033[m')
    return get_one(uid, UserModel, user_schema, 'user')


def delete_user(uid):
    logging.info('\033[1;34mDeleting one user\033[m')
    return delete(uid, UserModel, user_schema, 'user')


def update_user(uid):
    logging.info('\033[1;34mUpdating one user\033[m')
    user = gut_fields(uid)
    return update(user_schema, user['update'], 'user')


def post_user():
    logging.info('\033[1;34mCreating one new user\033[m')
    user = gut_fields()
    return post(user_schema, user['post'])


def validation_fields(name, phone, message):
    logging.info('\033[1;34mValidation fields\033[m')
    is_required(name, 'Write your name!')
    logging.info('\033[1;34mName valid\033[m')
    is_required(phone, 'Write your phone!')
    logging.info('\033[1;34mPhone valid\033[m')
    is_required(message, 'Write your message!')
    logging.info('\033[1;34mMessage valid\033[m')


def gut_fields(uid=''):
    logging.info('\033[1;34mGetting fields\033[m')
    name = request.json['name']
    phone = request.json['phone']
    message = request.json['message']
    validation_fields(name, phone, message)
    user_update = passed_data_fields_model(uid, name, phone, message)
    user_post = UserModel(name, phone, message)
    data = {'post': user_post, 'update': user_update}
    return data


def passed_data_fields_model(uid, name, phone, message):
    logging.info('\033[1;34mPassing the data\033[m')
    user = UserModel.query.get(uid)
    if not user:
        logging.info('\033[1;31mThere is no data!\033[m')
        return jsonify({'message': "user don't exist", 'data': {}}), 404
    user.update = datetime.datetime.now()
    user.name = name
    user.phone = phone
    user.message = message
    return user