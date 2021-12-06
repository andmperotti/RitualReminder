import tkinter as tk
from tkinter import ttk
import time
import datetime

clienttxt = 'C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt' #path to your Client.txt file

def popup():
    """Pops up a message to the user (which persists on top of the games window) when they interact with a Ritual to remind them to spend their tribute."""
    objectFinder = tk.Tk()
    objectFinder.wm_attributes("-topmost", 1) 
    logFrame = tk.LabelFrame(objectFinder, text="Ritual Reminder")
    logFrame.pack(fill="both", expand=True)
    menu_Label = ttk.Label(logFrame, text="SPEND YOUR TRIBUTE!")
    menu_Label.pack(expand=True)
    objectFinder.geometry(f"200x100+920+750") #the second 2 numbers are the postioning (X+Y) of pixels of the top left corner of the popup window.
    objectFinder.mainloop()

with open(clienttxt, encoding='utf-8') as f:
    f.seek(0,2)
    while True:
        line = f.readline()
        if "FindClosestObject" in line:
            print(f"Ritual Interacted with at:{datetime.datetime.now()}") #This prints out a record of rituals you clicked on in the terminal (command prompt) that will popup and run the script.
            popup()
        if not line:
            time.sleep(1) #This is the delay, (1 second). You can pass in .1 for tenth of a second, .5 half second, 2 for 2 seconds, etc.
            continue
