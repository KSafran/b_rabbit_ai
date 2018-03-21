import pandas as pd
from collect_rap_data import get_song_lyrics

song_data = pd.read_csv('rapper\data/top_rap_songs_10s.csv')
lyrics = [get_song_lyrics(song) for song in song_data['title']]
song_data['lyrics'] = lyrics
song_data.to_csv('rapper/data/songs_and_lyrics.csv', index=False)
