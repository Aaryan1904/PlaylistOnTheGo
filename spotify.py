from cgi import print_form
from unittest import result
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

class sp:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id=client_id
        self.client_secret=client_secret
        self.search= spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.client_id,
                                                           client_secret=self.client_secret))
    
    def getPlaylist(self, link) -> list:
        song_list = []
        playlist_name = ""
        success = True
        try:
            tmp = self.search.playlist(self.extractId(link), fields=None, market=None, additional_types=('track', ))
            playlist_name=tmp['name']
            for track in tmp['tracks']['items']:
                song_list.append(track['track']['name'] + " " + track['track']['album']['name'] + " " + track['track']['album']['artists'][0]['name'] + "Lyrical") 
        except Exception:
            print("Spotigy API Failure")
            print(Exception)
            success = False
        return song_list, playlist_name, success
            
    def extractId(self,link) -> str:
        tmp = link.split("/")
        if "?" in tmp[-1]:
            return tmp[-1].split("?")[0]
        return tmp[-1]



