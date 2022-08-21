from flask import Flask
import requests
from flask import request
from flask import Response
from analyser import RESPONSES
from analyser import USERS
from sound_2_text import get_rec_text


app = Flask(__name__)

TOKEN = "5458454629:AAHTr7Am8RJ71v2MsIxaviJHoGbB5OO7ucg"
PORTS_URL = "https://b227-82-80-173-170.eu.ngrok.io"
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'\
    .format(TOKEN, PORTS_URL)

MESSAGE = "Welcome to our bot server website. what are you doing here?"

@app.route("/")
def main():
    return MESSAGE

@app.route("/message", methods=["POST"])
def handle_message():
    print("got a message")
    message = request.get_json()
    chat_id = message['message']['chat']['id']
    ans = []
    if 'text' in message["message"]:
        ans = get_songs_from_shazam(message["message"]["text"])
    elif "sound" in message["message"]:
        txt = get_rec_text(message["message"]["sound"])
    return Response("message returned")


def analyse_message(words: list, chat_id: int) -> str:

    if chat_id in USERS:
        if words[0] in USERS[chat_id]:
            USERS[chat_id] = USERS[chat_id][words[0]]
    elif words[0] in RESPONSES:
        USERS[chat_id] = RESPONSES[words[0]]
    else:
        return "https://preply.com/en/online/english" \
               "%0AThis is a great website for study english." \
               "%0Awhen you finish, please come back to me and tell me what do you want."
    if type(USERS[chat_id]) == type(dict):
        analyse_message(words[1:], chat_id)
    else:
        USERS[chat_id](words[1:], chat_id)


if __name__ == "__main__":
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=1000)
