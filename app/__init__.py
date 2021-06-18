from flask import Flask, request, jsonify
from .settings.connection import connect_db
from .settings.config import config_db, config_ma, config_bp, secret_key
from bot.bot_telegram import send_message
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def create_app():
    logging.info('\033[1;34mInitialization a application\033[m')
    app = Flask(__name__)
    logging.info('\033[1;34mConnection database\033[m')
    connect_db(app)
    logging.info('\033[1;34mConfiguration database\033[m')
    config_db(app)
    logging.info('\033[1;34mConfiguration Marshmallow\033[m')
    config_ma(app)
    logging.info('\033[1;34mConfiguration blueprint\033[m')
    config_bp(app)
    secret_key(app)
    return app


logging.info('\033[1;34mExtending app\033[m')
app_ext = create_app()

@app_ext.route('/send', methods=['POST'])
def message():
    logging.info('\033[1;34mSending a message\033[m')
    name = request.json['name']
    chat_id = request.json['chat_id']
    msg = request.json['text']
    mock_request_data = {
        "message": msg,
        "chat_id": chat_id
    }
    response = requests.post('http://host.docker.internal:5000/messages', json=mock_request_data)
    if response.status_code != 201:
        logging.error('\033[1;31mError during send data to database!\033[m')
    else:
        logging.info('\033[1;34mData inserted to database with success\033[m')
    result = send_message(name, chat_id, msg)
    logging.info('\033[1;34mSend with success\033[m')
    return jsonify({'message': 'Sent with success', 'data': result}), 201
