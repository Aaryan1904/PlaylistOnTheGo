#Import the required Libraries
from cgitb import enable
from site import ENABLE_USER_SITE
import tkinter
from turtle import st
from youtube import yt
from tkinter import *
from tkinter import ttk

src = ""
dst = ""
#Create an instance of Tkinter frame
win=Tk()

#Set the geometry of Tkinter frame
win.geometry("550x350")

label_progress=Label(win, text="", font=("Courier 14"))
progress = ttk.Progressbar(win, orient = HORIZONTAL,
              length = 300, mode = 'determinate')
downloader=yt("AIzaSyAOh2GpAwgyROFvfh-PLuYv2fEK6eZSFrg", label_progress, progress, win)


def readFile(test_playlist):
        fileObj = open(test_playlist, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

# print(readFile("./test_playlist.txt"))

def extract_song(entry, label):
   button["state"] = DISABLED
   song_name=entry.get()
   link=downloader.search(song_name)
   label.configure(text=f"Downloading {song_name}...")
   if link:
        result=downloader.download(link)
   else:
        result = False
   if result:
            label.configure(text= f"{song_name} Download Successful!!! ")
   else:
            label.configure(text= "Download Failed...\nSounds like a you problem\nDeal with it!")
   button["state"] = NORMAL

#Title
title=Label(win, text="PlaylistOnTheGo", font=("Courier 22 bold"))
title.pack()

#Initialize a Label to display the User Input
label_song_hdr=Label(win, text="Enter Song Name", font=("Courier 20"))
label_song_hdr.pack()
label_result=Label(win, text="", font=("Courier 14"))
label_result.pack()
label_progress.pack()
progress.pack(pady = 10)

#Create an Entry widget to accept User Input
entry_song=Entry(win, width= 40)
entry_song.focus_set()
entry_song.pack()

#Create a Button to validate Entry Widget
button = Button(win, text= "Submit",width= 20, command=lambda:extract_song(entry_song, label_result))
button.pack(pady=20)

# #Initialize a Label to display the User Input
# label_src_hdr=Label(win, text="Enter Source", font=("Courier 22 bold"))
# label_src_hdr.pack()
label_src=Label(win, text="", font=("Courier 22 bold"))
label_src.pack()

# #Create an Entry widget to accept User Input
# entry_src=Entry(win, width= 40)
# entry_src.focus_set()
# entry_src.pack()


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