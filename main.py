from flask import Flask
import requests
from flask import request
from flask import Response
from analyser import RESPONSES


app = Flask(__name__)

TOKEN = "5458454629:AAHTr7Am8RJ71v2MsIxaviJHoGbB5OO7ucg"
PORTS_URL = "https://2a02-82-80-173-170.eu.ngrok.io"
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'\
    .format(TOKEN, PORTS_URL)

MESSAGE =""" Message """


@app.route("/")
def main():
    return MESSAGE

@app.route("/message", methods=["POST"])
def handle_message():
    print("got a message")
    message = request.get_json()
    chat_id = message['message']['chat']['id']
    res = requests.get('''https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'''
                       .format(TOKEN, chat_id, analyse_message(message["message"]["text"])))
    return Response("message returned")


def analyse_message(message: str) -> str:
    words = message.split(" ")
    if words[0] in RESPONSES:
        return RESPONSES[words[0]](words[1:])
    else:
        return "Bitch what do you want from me?!?!"


if __name__ == "__main__":
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=1000)
