import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

def extract_elements(html, class_):
    element_list = html.find_all('div', class_=class_)
    return [re.sub('\n', '', element.get_text()) for element in element_list]

def get_100_rap_songs(year):
    response = requests.get('https://www.billboard.com/charts/year-end/{}/hot-r-and-and-b-hip-hop-songs'.format(str(year)))
    html = BeautifulSoup(response.text)
    songs = extract_elements(html, 'ye-chart-item__title')
    artists = extract_elements(html, 'ye-chart-item__artist')
    song_data = pd.DataFrame.from_records({'title':songs, 'artist':artists})
    song_data['year'] = year
    return song_data

if __name__=='__main__':
    top_rap_songs = [get_100_rap_songs(year) for year in range(2010, 2018)]
    rap_df = pd.concat(top_rap_songs)
    rap_df.to_csv('rapper/data/top_rap_songs_10s.csv', index=False)
