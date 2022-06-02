import googleapiclient.discovery
from youtube_dl import YoutubeDL

class yt:
    def __init__(self, key: str):
        self.key = key
        self.audio_downloader = YoutubeDL({'format':'bestaudio'})
        api_service_name = "youtube"
        api_version = "v3"
        self.client = googleapiclient.discovery.build(api_service_name, api_version, developerKey = key)


    def download(self, link: str) -> bool:
        while True:
            try:
                print('Youtube Downloader'.center(40, '_'))
                self.audio_downloader.extract_info(link)

            except Exception:
                print("Couldn\'t download the audio")
                print(Exception)
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
        try:
            response = request.execute()
            #print(response)
            return f"https://www.youtube.com/watch?v={response['items'][0]['id']['videoId']}"
        except:
            return False

# test = yt("AIzaSyAOh2GpAwgyROFvfh-PLuYv2fEK6eZSFrg")
# tmp = test.search("tu jo mila")
# test.download(tmp)