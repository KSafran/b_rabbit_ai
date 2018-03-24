import re
import json
import markovify

with open('rapper/data/billboard_100_bigram_model.json', 'r') as model:
    song_model_json = model.read()

song_model = markovify.Chain.from_json(song_model_json)

def sing():
    song = []
    while len(song) < 30:
        song = song + song_model.walk()

    song = ' '.join(song)
    # remove beginning and ending sections/lines
    song = re.sub('^xxsectionxx ', '', song)
    song = re.sub('^xxlinexx ', '', song)
    song = re.sub('xxsectionxx$', '', song)
    song = re.sub('xxlinexx$', '', song)

    song = re.sub(' xxsectionxx ', '\r\n\r\n', song)
    song = re.sub(' xxlinexx ', '\r\n', song)
    print(song)
    return song
