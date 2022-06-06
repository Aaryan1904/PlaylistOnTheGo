#Import the required Libraries
from cgitb import enable
from site import ENABLE_USER_SITE
import tkinter
from turtle import st
from youtube import yt
from tkinter import *
from tkinter import ttk
from spotify import sp

src = ""
dst = ""
#Create an instance of Tkinter frame
win=Tk()

#Set the geometry of Tkinter frame
win.geometry("700x450")

label_progress=Label(win, text="", font=("Courier 14"))
progress = ttk.Progressbar(win, orient = HORIZONTAL,
              length = 300, mode = 'determinate')
downloader=yt("AIzaSyAOh2GpAwgyROFvfh-PLuYv2fEK6eZSFrg", label_progress, progress, win)
songs_playlist=sp("1dc31604dc65456fb345838959ef1c57", "b1f42367a6d84633867ccd9b4e522d3c")

def readFile(test_playlist):
        fileObj = open(test_playlist, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

# print(readFile("./test_playlist.txt"))

def extract_song(entry, label):
   button_song["state"] = DISABLED
   song_name=entry.get()
   link=downloader.search(song_name + " " + "lyrical")
   label.configure(text=f"Downloading {song_name}...")
   if link:
        result=downloader.download(link)
   else:
        result = False
   if result:
            label.configure(text= f"{song_name} Download Successful!!! ")
   else:
            label.configure(text= "Download Failed...\nSounds like a you problem\nDeal with it!")
   button_song["state"] = NORMAL

def extract_playlist(entry, label):
     button_playlist["state"] = DISABLED
     playlist_link=entry.get()
     print(playlist_link)
     arr=songs_playlist.getPlaylist(playlist_link)
     for i in arr:
          link=downloader.search(i)
          label.configure(text=f"Downloading {i}...")
          if link:
               result=downloader.download(link)
          else:
               result = False
          if result:
               label.configure(text= f"{i} Download Successful!!! ")
          else:
               label.configure(text= "Download Failed...\nSounds like a you problem\nDeal with it!")
     button_playlist["state"] = NORMAL

#Title
title=Label(win, text="PlaylistOnTheGo", font=("Courier 22 bold"))
title.pack()

#Initialize a Label to display the User Input
label_song_hdr=Label(win, text="Enter Song Name", font=("Courier 20"))
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

label_playlist_hdr=Label(win, text="Enter  Spotify playlist link", font=("Courier 20"))
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

# #Create a Button to validate Entry Widget
# ttk.Button(win, text= "Submit",width= 20, command=lambda:display_text(entry_src, label_src, src)).pack(pady=20)

# #Initialize a Label to display the User Input
# label_dst_hdr=Label(win, text="Enter Destination", font=("Courier 22 bold"))
# label_dst_hdr.pack()
# label_dst=Label(win, text="", font=("Courier 22 bold"))
# label_dst.pack()

# #Create an Entry widget to accept User Input
# entry_dst=Entry(win, width= 40)
# entry_dst.focus_set()
# entry_dst.pack()

# #Create a Button
# ttk.Button(win, text= "Submit",width= 20, command=lambda:display_text(entry_dst, label_dst, dst)).pack(pady=20)

win.mainloop()