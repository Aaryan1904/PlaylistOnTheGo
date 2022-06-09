#Import the required Libraries
from tabnanny import check
import tkinter
from youtube import yt
from tkinter import *
from tkinter import ttk
from spotify import sp
import os
from tkinter import filedialog
import subprocess
import signal
import sys
original = sys.stdout
sys.stdout = open('PlaylistOnTheGo_log.txt', 'w')

YOUTUBE_KEY=""
SPOTIFY_CLIENT_KEY=""
SPOTIFY_SECRET_KEY=""
ILLIGAL_CHARS=["'","/",'"', "\\",'*','?',":", "|"]

#Create an instance of Tkinter frame
win=Tk()

#Set the geometry of Tkinter frame
win.geometry("800x500")
win.title('PlaylistOnTheGo')

label_progress=Label(win, text="", font=("Courier 14"))
progress = ttk.Progressbar(win, orient = HORIZONTAL,
              length = 300, mode = 'determinate')

downloader=yt(YOUTUBE_KEY, label_progress, progress, win)
songs_playlist=sp(SPOTIFY_CLIENT_KEY, SPOTIFY_SECRET_KEY)


def readFile(test_playlist):
        fileObj = open(test_playlist, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

def extract_song(entry, label):
   downloader.cancel = False
   button_playlist["state"] = DISABLED
   button_song["state"] = DISABLED
   song_name=entry.get()
   check = True
   if "http" in song_name or "www" in song_name:
        link = song_name
   else:     
        link,check=downloader.search(song_name + " " + "lyrical")
   label.configure(text=f"Downloading {song_name}...")
   if check:
        result=downloader.download(link)
   else:
        result = False
   if result:
            label.configure(text= f"{song_name} Download Successful!!! ")
   else:
            label.configure(text= "Download Failed...\nSounds like a you problem\nDeal with it!")
   button_playlist["state"] = NORMAL
   button_song["state"] = NORMAL

def extract_playlist(entry, label):
     downloader.cancel = False
     button_song["state"] = DISABLED
     button_playlist["state"] = DISABLED
     playlist_link=entry.get()
     check = True
     print(playlist_link)
     arr, playlist_name, check=songs_playlist.getPlaylist(playlist_link)
     if check is False:
        label.configure(text= "Download Failed...\nSounds like a you problem\nDeal with it!")
        button_song["state"] = NORMAL
        button_playlist["state"] = NORMAL
        return
     for i in ILLIGAL_CHARS:
          playlist_name = playlist_name.replace(i,"")
     if not os.path.exists(playlist_name):
         print(playlist_name)
         os.makedirs(playlist_name)
     os.chdir('./' + playlist_name)
     for i in arr:
          link, check=downloader.search(i)
          label.configure(text=f"Downloading {i}...")
          if check:
               result=downloader.download(link)
          else:
               result = False
          if result is not False:
               label.configure(text= f"{i} Download Successful!!! ")
          else:
               label.configure(text= "Download Failed...\nSounds like a you problem\nDeal with it!")
               break
     os.chdir('..')
     button_song["state"] = NORMAL
     button_playlist["state"] = NORMAL

# def cancel():
#      button_song["state"] = NORMAL
#      button_playlist["state"] = NORMAL
#      downloader.reset()
#      if os.path.isfile(downloader.last_song):
#           os.remove(downloader.last_song)

#Title
title=Label(win, text="PlaylistOnTheGo", font=("Courier 22 bold"))
title.pack()

#Initialize a Label to display the User Input
label_song_hdr=Label(win, text="Enter Song Name \n (enter exact YouTube link of \n the desired song to get accurate results)", font=("Courier 16"))
label_song_hdr.pack()


#Create an Entry widget to accept User Input
entry_song=Entry(win, width= 40)
entry_song.focus_set()
entry_song.pack()

#Create a Button to validate Entry Widget
button_song = Button(win, text= "Submit",width= 20, command=lambda:extract_song(entry_song, label_result))
button_song.pack(pady=20)

# #Initialize a Label to display the User Input
label_src=Label(win, text="", font=("Courier 22 bold"))
label_src.pack()

label_playlist_hdr=Label(win, text="Enter  Spotify playlist link", font=("Courier 16"))
label_playlist_hdr.pack()

# #Create an Entry widget to accept User Input
entry_playlist=Entry(win, width= 40)
entry_playlist.focus_set()
entry_playlist.pack()

#Create a Button to enter playlist
button_playlist = Button(win, text= "Submit",width= 20, command=lambda:extract_playlist(entry_playlist, label_result))
button_playlist.pack(pady=20)

label_result=Label(win, text="", font=("Courier 14"))
label_result.pack(pady=10)
label_progress.pack()
progress.pack(pady = 10)

#Create a Button to cancel the current download
# button_cancel = Button(win, text= "Cancel",width= 20, command=cancel)
# button_cancel.pack(pady=20)


win.mainloop()
sys.stdout = original