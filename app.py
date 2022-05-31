#Import the required Libraries
from tkinter import *
from tkinter import ttk

src = ""
dst = ""
#Create an instance of Tkinter frame
win=Tk()

#Set the geometry of Tkinter frame
win.geometry("550x350")

def display_text(entry, label, var):
   string=entry.get()
   label.configure(text=string)
   var = string
   
#Initialize a Label to display the User Input
label_src_hdr=Label(win, text="Enter Source", font=("Courier 22 bold"))
label_src_hdr.pack()
label_src=Label(win, text="", font=("Courier 22 bold"))
label_src.pack()

#Create an Entry widget to accept User Input
entry_src=Entry(win, width= 40)
entry_src.focus_set()
entry_src.pack()


#Create a Button to validate Entry Widget
ttk.Button(win, text= "Submit",width= 20, command=lambda:display_text(entry_src, label_src, src)).pack(pady=20)

#Initialize a Label to display the User Input
label_dst_hdr=Label(win, text="Enter Destination", font=("Courier 22 bold"))
label_dst_hdr.pack()
label_dst=Label(win, text="", font=("Courier 22 bold"))
label_dst.pack()

#Create an Entry widget to accept User Input
entry_dst=Entry(win, width= 40)
entry_dst.focus_set()
entry_dst.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Submit",width= 20, command=lambda:display_text(entry_dst, label_dst, dst)).pack(pady=20)

win.mainloop()