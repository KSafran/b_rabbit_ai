import pandas as pd
import re
import markovify
from nltk import word_tokenize, download
download('punkt')


def format_lyrics(lyric):
    lyric = re.sub('\r\n\r\n', ' xxsectionxx ', lyric) # delimit verses
    lyric = re.sub('\r\n', ' xxlinexx ', lyric) # delimit lines
    lyric = re.sub('\[[()&a-zA-Z0-9 :.-]+\]', '', lyric) # remove notes in []
    # need to only remove individual [] sets, not things between two notes
    lyric = lyric.lower()
    lyric = re.sub("'", '', lyric)
    lyric = re.sub("\x92", '', lyric)
    lyric = word_tokenize(lyric)
    return lyric

if __name__=='__main__':
    song_data = pd.read_csv('rapper/data/songs_and_lyrics.csv', encoding = "ISO-8859-1")
    song_data['lyrics'] = [format_lyrics(lyric) for lyric in song_data['lyrics']]
