from cgitb import text
import googleapiclient.discovery
from youtube_dl import YoutubeDL
import os


class yt:
    def __init__(self, key: str, label, progress, frame):
        self.label = label
        self.key = key
        self.audio_downloader = YoutubeDL({'format':'bestaudio', 'progress_hooks': [self.my_hook]})
        api_service_name = "youtube"
        api_version = "v3"
        self.client = googleapiclient.discovery.build(api_service_name, api_version, developerKey = key)
        self.progress = progress
        self.frame = frame
        self.last_song = ""
        self.cancel = False

    def download(self, link: str) -> bool:
        while True:
            try:
                print('Youtube Downloader'.center(40, '_'))
                self.audio_downloader.extract_info(link)

            except Exception as e:
                print("Couldn\'t download the audio")
                print(e)
                return False
            break
        return True
    
    def search(self, song: str) -> str:
        request = self.client.search().list(
                part="id,snippet",
                type='video',
                q=song,
                videoDuration='short',
                maxResults=30
        )
        print(song)
        response = ""
        try:
            response = request.execute()
            return f"https://www.youtube.com/watch?v={response['items'][0]['id']['videoId']}" , True
        except Exception as e:
            print("Youtube Search Failed")
            print(response)
            print(e)
            return "", False

    def my_hook(self, d):
        if d['status'] == 'finished':
            pass
        if d['status'] == 'downloading':
            self.progress['value'] = int(float(d['_percent_str'][:-1]))
            self.last_song = d['tmpfilename']
        if self.cancel:
            os.abort()
        self.frame.update()

    def reset(self):
        self.progress['value'] = 0
        self.label.configure(text="Download Cancelled")
        self.cancel = True
        
