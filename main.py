from flask import Flask
import requests
from flask import request
from flask import Response
app = Flask(__name__)

TOKEN = "5458454629:AAHTr7Am8RJ71v2MsIxaviJHoGbB5OO7ucg"
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://86c6-2a02-6680-1105-449e-885c-5f07-c22b-963d.eu.ngrok.io/message'.format(TOKEN)

MESSAGE ="""
a. The first part of the url, is the server domain, we got it from ngrok\n
b. The second part is the path, the route which we will define in our server. In this case we chose message
"""


@app.route("/")
def main():
    return MESSAGE

@app.route("/message", methods=["POST"])
def handle_message():
    print("got a message")
    chat_id = request.get_json()['message']['chat']['id']
    res = requests.get('''https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'''.format(TOKEN, chat_id, "Got it"))
    return Response("success")

if __name__ == "__main__":
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=1000)
