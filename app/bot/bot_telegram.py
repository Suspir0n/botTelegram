import logging
from telegram import Update, ForceReply, KeyboardButton, ReplyKeyboardMarkup, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from ..settings.config import config_telegram
from flask import Response, request
from datetime import datetime
from ..routes.user_routes import post_user
import json


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def send_message(username, chat_id):
    bot_token = config_telegram()
    bot_chatID = chat_id
    bot_message = f'Hello {username}'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    return request.get(send_text)


def handle_message_request(update: Update, context: CallbackContext):
    contact = update.effective_message.contact
    phone = contact.phone_number
    user = update.effective_user
    username = user.mention_markdown_v2()
    chat_uid = update.message.chat_id
    mock_request_data = {
        "uid": 1,
        "data": {
            "name": username,
            "phone": phone,
            "chat_id": chat_uid,
        },
        "date": datetime.now().timestamp()
    }
    json_string = json.dumps(mock_request_data, ensure_ascii=False)
    reponse = Response(json_string, content_type="application/json; charset=utf-8")
    update.message.reply_text(
        "Thank you!",
        reply_markup=ForceReply(selective=True))
    return post_user(reponse)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    contact_keyboard = KeyboardButton("Share contact", request_contact=True)
    custom_keyboard = [[contact_keyboard]]  # creating keyboard object
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    update.message.reply_text(
        "Would you mind sharing your contact with me?",
        reply_markup=reply_markup)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def message(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    message = get_client_message_response(update.message.text)
    update.message.reply_text(message + f', seu chat_id: {uid}')


def get_client_message_response(client_data):
    message_response = search_message(client_data)
    if not message_response:
        return "No understand, ask again"
    return message_response


def search_message(client_message):
    messages_responses = [
        {"hello": "hello my friend"},
        {"what is your name?": "Bo Codin"},
        {"how are you?": "I'm me fine, and you?"},
        {"fine too": "Nice Nice Nice"},
        {"what are you doing?": "nothing"},
    ]
    response = str()
    for value in messages_responses:
        if not client_message in value:
            continue
        response = value[client_message]
    return response


def main() -> None:
    """Start the bot."""
    token = config_telegram()
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_message_request))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    updater.start_polling()
    updater.idle()
