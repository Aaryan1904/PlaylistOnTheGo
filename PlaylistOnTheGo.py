from tkinter import filedialog
from tkinter import *
import os



win = Tk()
win.geometry('750x150')
win.title('PlaylistOnTheGo')

f = ("Times bold", 9)

def nextPage():
    win.destroy()
    import app

def extractDest():
    os.chdir(filedialog.askdirectory())
    nextPage()

# #Initialize a Label to display the User Input
label_dest_hdr=Label(win, text="Select the Folder to store the song or playlist", font=("Courier 14"))
label_dest_hdr.pack()

# #Create a Button to validate Entry Widget
button_song = Button(win, text= "Select Folder",width= 20, command=extractDest)
button_song.pack(pady=20)


win.mainloop()
