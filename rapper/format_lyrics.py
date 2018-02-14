import pandas as pd
import re
import markovify
from nltk import word_tokenize, download
download('punkt')

song_data = pd.read_csv('rapper/data/songs_and_lyrics.csv', encoding = "ISO-8859-1")

def format_lyrics(lyric):
    lyric = re.sub('\r\n\r\n', ' {section} ', lyric) # delimit verses
    lyric = re.sub('\r\n', ' {line} ', lyric) # delimit lines
    lyric = re.sub('\[.*\]', '', lyric) # remove notes
    lyric = lyric.lower()
    lyric = word_tokenize(lyric)
    return lyric

song_data['lyrics'] = [format_lyrics(lyric) for lyric in song_data['lyrics']]
