import logging
from telegram import Update, ForceReply, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import json
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def send_message(username, chat_id, msg):
    bot_token = '1529947213:AAEbABEEdleAfYpAQYxkuUF4H5L_5-FsLgg'
    bot_chatID = chat_id
    bot_message = f'{msg}{username}'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.text


def handle_message_request(update: Update, context: CallbackContext):
    contact = update.effective_message.contact
    phone = contact.phone_number
    user = update.effective_user
    profile = user.mention_markdown_v2()
    name = ''
    for letter in profile:
        if letter == ']':
            break
        if letter != '[':
            name += letter
    chat_uid = update.message.chat_id
    mock_request_data = {
        "data": {
            "name": name,
            "phone": phone,
            "chat_id": chat_uid,
        },
        "date": datetime.now().timestamp()
    }
    # json_string = json.dumps(mock_request_data, ensure_ascii=False)
    response = requests.post('http://host.docker.internal:5000/users', json=mock_request_data)
    if response.status_code != 201:
        logging.error('\033[1;31mError during send data to database!\033[m')
    else:
        logging.info('\033[1;34mData inserted to database with success\033[m')
    update.message.reply_text(
        "Thank you!\nWhat are you doing ?",
        reply_markup=ForceReply(selective=True))


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
    update.message.reply_text(message)


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
        {"nothing": "nice nice"},
        {"nothing, and you?": "nothing"},

    ]
    response = str()
    for value in messages_responses:
        if not client_message in value:
            continue
        response = value[client_message]
    return response


def main() -> None:
    """Start the bot."""
    logging.info('\033[1;34mInitialization bot\033[m')
    updater = Updater('1529947213:AAEbABEEdleAfYpAQYxkuUF4H5L_5-FsLgg')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_message_request))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()