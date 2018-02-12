import requests
import globals
from bs4 import BeautifulSoup
import re

def get_song_data(song_title):
    search_url = globals.GENIUS_URL + "/search"
    params = {'q': song_title}
    return requests.get(search_url, params=params,
                            headers=globals.HEADERS)

def get_song_lyrics(song_title):
    song_data = get_song_data(song_title)
    song_data = song_data.json()
    # import pdb
    # pdb.set_trace()
    song_path = song_data["response"]["hits"][0]['result']['api_path']

    page = requests.get("http://genius.com" + song_path)
    html = BeautifulSoup(page.text, "html.parser")
    #remove script tags that they put in the middle of the lyrics
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()
    re.sub('\[.*\]', '', lyrics) # rap genius has notes in brackets
    return lyrics
