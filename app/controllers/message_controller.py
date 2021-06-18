import datetime
from flask import request, jsonify
from ..models.message_model import MessageModel
from ..schemas.message_serealize import message_schema, messages_schema
from .base_controller import get_all, get_one, delete, post, update
from ..notify.base_notification import is_required
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def get_messages():
    logging.info('\033[1;34mGetting all messages\033[m')
    return get_all(MessageModel, messages_schema, 'message')


def get_message(uid):
    logging.info('\033[1;34mGetting one message\033[m')
    return get_one(uid, MessageModel, message_schema, 'message')


def delete_message(uid):
    logging.info('\033[1;34mDeleting one message\033[m')
    return delete(uid, MessageModel, message_schema, 'message')


def update_message(uid):
    logging.info('\033[1;34mUpdating one message\033[m')
    message = got_fields(uid)
    return update(message_schema, message['update'], 'message')


def post_message():
    logging.info('\033[1;34mCreating one new message\033[m')
    message = got_fields()
    return post(message_schema, message['post'])


def validation_fields(message, chat_id):
    logging.info('\033[1;34mValidation fields\033[m')
    is_required(message, 'Write your name!')
    logging.info('\033[1;34mMessage valid\033[m')
    is_required(str(chat_id), 'Write uid chat')
    logging.info('\033[1;34mChat_id valid\033[m')


def got_fields(uid=''):
    logging.info('\033[1;34mGetting fields\033[m')
    message = request.json['message']
    chat_id = request.json['chat_id']
    validation_fields(message, chat_id)
    message_update = passed_data_fields_model(uid, message, chat_id)
    message_post = MessageModel(message, chat_id)
    data = {'post': message_post, 'update': message_update}
    return data


def passed_data_fields_model(uid, message, chat_id):
    logging.info('\033[1;34mPassing the data\033[m')
    msg = MessageModel.query.get(uid)
    if not msg:
        logging.info('\033[1;31mThere is no data!\033[m')
        return jsonify({'message': "message don't exist", 'data': {}}), 404
    message.update = datetime.datetime.now()
    message.message = message
    message.chat_id = chat_id
    return message