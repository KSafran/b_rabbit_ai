import pandas as pd
import markovify
import format_lyrics

song_data = pd.read_csv('rapper/data/songs_and_lyrics.csv', encoding = "ISO-8859-1")
song_data['lyrics'] = [format_lyrics.format_lyrics(lyric) for lyric in song_data['lyrics']]

song_model = markovify.Chain(song_data['lyrics'], state_size=2)
with open('rapper/data/billboard_100_bigram_model.json', 'w') as model:
    model.write(song_model.to_json())
