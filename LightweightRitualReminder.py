import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import time
import configparser
from tkinter.filedialog import askopenfilename
import datetime
import os

clienttxt = 'C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt' #path to your Client.txt file

def popup():
    """Pops up a message to the user when they interact with a Ritual to remind them to spend their tribute."""
    objectFinder = tk.Tk()
    objectFinder.wm_attributes("-topmost", 1) #Persists over other windows
    logFrame = tk.LabelFrame(objectFinder, text="Ritual Reminder")
    logFrame.pack(fill="both", expand=True)
    menu_Label = ttk.Label(logFrame, text="SPEND YOUR TRIBUTE!")
    menu_Label.pack(expand=True)
    objectFinder.geometry(f"200x100+920+750") #the second 2 numbers are the postioning (X+Y) of pixels of the top left of the popup.
    objectFinder.mainloop()

with open(clienttxt, encoding='utf-8') as f:
    f.seek(0,2)
    while True:
        line = f.readline()
        if "FindClosestObject" in line:
            print(f"Ritual Interacted with at:{datetime.datetime.now()}") #This prints out a record of rituals you clicked on in the terminal that will popup and run the script.
            popup()
        if not line:
            time.sleep(1) #This is the delay, 1 second if it annoys you, then you can set it to 0.5 for half a second, etc.
            continue
