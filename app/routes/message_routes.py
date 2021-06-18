from flask import Blueprint, jsonify
from ..controllers import message_controller
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

bp_messages = Blueprint('messages', __name__)


@bp_messages.route('/messages', methods=['GET'])
def get_messages():
    return message_controller.get_messages()


@bp_messages.route('/messages/<uid>', methods=['GET'])
def get_message(uid):
    return message_controller.get_message(uid)


@bp_messages.route('/messages', methods=['POST'])
def post_message():
    return message_controller.post_message()


@bp_messages.route('/messages/<uid>', methods=['DELETE'])
def delete_messages(uid):
    return message_controller.delete_message(uid)


@bp_messages.route('/messages/<uid>', methods=['PUT'])
def update_messages(uid):
    return message_controller.update_message(uid)