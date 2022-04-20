from importlib.resources import path
import lyricsgenius
import pandas as pd
import json

GENIUS_ACCESS_TOKEN = 'YMANOmvvh0bmAhtflFXj8yjhLe8rY2Ok0YwJnteYSEkKt3HJYvyujFaO15Flnrmf'

# Get the lyrics of 20 songs from the top 20 songs of the Billboard Hot 100
def get_lyrics(artist, max_songs=20):
    genius = lyricsgenius.Genius(
        GENIUS_ACCESS_TOKEN, timeout=10, remove_section_headers=True
    )
    artist_data = genius.search_artist(
        artist, max_songs=max_songs, sort="popularity"
    )

    # Get the songs
    songs = artist_data.songs
    data = {}
    for song in songs:
        song_obj = {}

        song_obj['title'] = song.title
        song_obj['id'] = song.id
        song_obj['url'] = song.url
        song_obj['lyrics'] = song.lyrics

        data[song.title] = song_obj

    return data

# Get the lyrics of the top 20 songs of the given artists
def main():
    artists = ['The Beatles', 'Kanye', 'Taylor Swift', 'Jack Harlow', 'Adele']
    artist_data = {}

    for artist in artists:
        artist_data[artist] = get_lyrics(artist)

    # Save the_beatles to a json file
    with open('data.json', 'w') as f:
        json.dump(artist_data, f)
