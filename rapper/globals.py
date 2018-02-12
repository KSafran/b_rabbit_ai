GENIUS_URL = "http://api.genius.com"
with open('rapper/data/rap_genius_api.txt', 'r') as token_file:
    TOKEN = token_file.read()
HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}
