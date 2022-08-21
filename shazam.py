import requests
import json
from typing import List


def get_song_from_shazam(text: str) -> List:
    res = []
    url = "https://shazam.p.rapidapi.com/search"

    querystring = {"term": text,
                   "locale": "en-US",
                   "offset": "0",
                   "limit": "8"
                   }
    headers = {
    "X-RapidAPI-Key": "34d6382fc3mshbbc556b33d0441bp1dc3ebjsnc2fcb22075fc",
    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_object = json.loads(response.text)
    tracks = json_object['tracks']
    for hit in tracks["hits"]:
        res += [hit["track"]["title"] + " by " + hit["track"]["subtitle"] + " " + hit["track"]["url"]]
    print(res)
    return res


if __name__ == "__main__":
    get_song_from_shazam("hello")