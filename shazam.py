# from ShazamAPI import Shazam
#
# mp3_file_content_to_recognize = open(r'C:\Users\Shay Tobi\PycharmProjects\telegram-bot-telegram_bot_group_6\sky_full_of_stars.mp3', 'rb').read()
#
# shazam = Shazam(mp3_file_content_to_recognize)
#
# recognize_generator = shazam.recognizeSong()
# while True:
#     print(next(recognize_generator))  # current offset & shazam response to recognize requests
from pydub import AudioSegment
# import base64
# import requests
# import json
#
# file_path = r"C:\Users\Shay Tobi\PycharmProjects\telegram-bot-telegram_bot_group_6\sky_full_of_stars.mp3"
# url = "https://rapidapi.p.rapidapi.com/songs/detect"
# encode_string = base64.b64encode(open(file_path, "rb").read())
# payload = encode_string
#
# headers = {
#     'content-type': "text/plain",
#     'x-rapidapi-key': "34d6382fc3mshbbc556b33d0441bp1dc3ebjsnc2fcb22075fc",
#     'x-rapidapi-host': "shazam.p.rapidapi.com"
# }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
"""
import requests

url = "https://shazam.p.rapidapi.com/search"

querystring = {"term":" sky full",
			   "locale": "en-US",
			   "offset": "0",
			   "limit":"5"
			   }

headers = {
	"X-RapidAPI-Key": "34d6382fc3mshbbc556b33d0441bp1dc3ebjsnc2fcb22075fc",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}
"""
from shazamio import Shazam
import asyncio
import http.client
SONG_PATH = r"sky_full_of_stars.ogg"
conn = http.client.HTTPSConnection("shazam.p.rapidapi.com")

async def search():
    shazam = Shazam()
    out = await shazam.recognize_song("sky_full_of_stars.ogg")
    print(out)

payload = "\"Generate one on your own for testing and send the body with the content-type as text/plain\""

headers = {
    'content-type': "text/plain",
    'X-RapidAPI-Key': "34d6382fc3mshbbc556b33d0441bp1dc3ebjsnc2fcb22075fc",
    'X-RapidAPI-Host': "shazam.p.rapidapi.com"
    }

conn.request("POST", "/songs/v2/detect?timezone=America%2FChicago&locale=en-US", payload, headers)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(search())
