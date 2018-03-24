import requests
import globals
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_song_data(song_title):
    search_url = globals.GENIUS_URL + "/search"
    params = {'q': song_title}
    return requests.get(search_url, params=params,
                            headers=globals.HEADERS)

def get_song_lyrics(song_title):
    print('getting lyrics for ' + song_title)
    song_data = get_song_data(song_title)
    song_data = song_data.json()
    song_path = song_data["response"]["hits"][0]['result']['api_path']

    page = requests.get("http://genius.com" + song_path)
    html = BeautifulSoup(page.text, "html.parser")
    #remove script tags that they put in the middle of the lyrics
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()
    re.sub('\[.*\]', '', lyrics) # rap genius has notes in brackets
    return lyrics

if __name__=='__main__':
    song_data = pd.read_csv('rapper/data/top_rap_songs_10s.csv')
    song_data['lyrics'] = [get_song_lyrics(song) for song in song_data['title']]
    song_data.to_csv('rapper/data/songs_with_lyrics.csv', index=False)
