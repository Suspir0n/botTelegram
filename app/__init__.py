from flask import Flask, request, jsonify
from .settings.connection import connect_db
from .settings.config import config_db, config_ma, config_bp, secret_key
from bot.bot_telegram import send_message
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
    result = send_message(name, chat_id, msg)
    logging.info('\033[1;34mSend with success\033[m')
    return jsonify({'message': 'Sent with success', 'data': result}), 201
