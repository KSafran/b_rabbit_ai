import spotipy
name = '2 Chainz'
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print(results)
