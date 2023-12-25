import requests, os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Environment variables
CLIENT_ID_SPOTIFY= os.environ.get("CLIENT_ID_SPOTIFY")
CLIENT_SECRET_SPOTIFY= os.environ.get("CLIENT_SECRET_SPOTIFY")

# Scraping Billboard 100
date=input("Which year do you want to travel to? Type the data in the format YYYY-MM-DD: ")
# billboard url website
URL=f"https://www.billboard.com/charts/hot-100/{date}/"
response=requests.get(url=URL)
billboard_web_page=response.text
soup=BeautifulSoup(billboard_web_page,"html.parser")
songs=soup.select(selector="li ul li h3")

list_of_songs=[song.getText().strip() for song in songs]
print(list_of_songs)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID_SPOTIFY,
        client_secret=CLIENT_SECRET_SPOTIFY,
        show_dialog=True,
        cache_path="token.txt",
        username="Arnold Çobo",
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)