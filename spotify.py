import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube import yt

class sp:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id=client_id
        self.client_secret=client_secret
        self.search= spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.client_id,
                                                           client_secret=self.client_secret))
    
    def getPlaylist(self, link) -> list:
        tmp = self.search.playlist(self.extractId(link), fields=None, market=None, additional_types=('track', ))
        song_list=[]
        for track in tmp['tracks']['items']:
            song_list.append(track['track']['name'] + " " + track['track']['album']['name'] + " " + track['track']['album']['artists'][0]['name'])
        return song_list
            
    def extractId(self,link) -> str:
        tmp = link.split("/")
        if "?" in tmp[-1]:
            return tmp[-1].split("?")[0]
        return tmp[-1]

        
# test= sp("1dc31604dc65456fb345838959ef1c57", "b1f42367a6d84633867ccd9b4e522d3c")

# results = test.search.search(q='The Weekend', limit=3)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track["name"])



    # print(track['track']['name'], track['track']['album']['name'], track['track']['album']['artists'][0]['name'])
    #print(idx, track['track']['name'], track['track']['album']['name'], track['track']['album']['artists'][0]['name'])
#print(tmp["tracks"]["items"])
# print(song_list)

# test = "https://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl"
# test = test.split("/")
# print(test)
# if "?" in test[-1]:
#     print(test[-1].split("?")[0])
# else: 
#     print(test[-1])

# playlist(playlist_id, fields=None, market=None, additional_types=('track', ))
#     2DHKR2hBKZ8z9REgTBbNeu
# https://open.spotify.com/playlist/14ZWFMHw5a4cIOWz5qxjPB?si=4122ebdb54284883
#https://open.spotify.com/playlist/14ZWFMHw5a4cIOWz5qxjPB?si=50ada01ad9624ec0
#ttps://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl?si=d84de3ca09264768
# https://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl?si=43ec7add23344a2e
# https://open.spotify.com/playlist/37i9dQZF1DX9oegrjMzKDW?si=93efde41f9da4f69
# res: {
#     "travkd": {
#         "itrmd": [

#         ]
#     }
# }