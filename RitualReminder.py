"""A program that alerts Path of Exile players when they interact with a Ritual. Players are reminded with a persistent pop (made with tkinter module) up to spend their tribute. This script only reads your Client.txt file and for that reason is not against the TOS of Path of Exile."""

#Import modules needed for program
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import time
import configparser
from tkinter.filedialog import askopenfilename

#Setting up some shortcuts/global variables to use in our code
config = configparser.ConfigParser()
x_location = None
y_location = None

def popup():
    """Pops up a message to the user when they interact with a Ritual to remind them to spend their tribute."""
    objectFinder = tk.Tk()
    objectFinder.wm_attributes("-topmost", 1) #Persists over other windows
    logFrame = tk.LabelFrame(objectFinder, text="Ritual Reminder")
    logFrame.pack(fill="both", expand=True)
    menu_Label = ttk.Label(logFrame, text="SPEND YOUR TRIBUTE!")
    menu_Label.pack(expand=True)
    objectFinder.geometry(f"200x100+{x_location}+{y_location}")
    objectFinder.mainloop()

# def running_pop():
#     """Creates a small tkinter window telling the user the script is running."""
#     running = tk.Tk()
#     runningFrame = tk.LabelFrame(running, text="Ritual Reminder")
#     runningFrame.pack()
#     runningMenu = ttk.Label(runningFrame, text='Running')
#     runningMenu.pack()

def read_file(clienttxt):
    """Reads client.txt file constantly for "FindClosestObject"."""
    f = open(clienttxt)
    f.seek(0,2)
    while True:
        line = f.readline()
        if "FindClosestObject" in line:
            popup()
        if not line:
            time.sleep(0.1)
            continue

def set_client_location():
    """Asks user to select location of client.txt file."""
    tk.Tk().withdraw() #
    filename = askopenfilename()
    config['SETTINGS']['ClientFileLocation'] = filename
    with open('RitualReminderClientLocation.ini', 'w') as configfile:
        config.write(configfile)


def set_up_popup_location():
    """Lets the user define where they want their reminder popup to be located."""

    #define functions that will be used inside our settings gui
    def save_pop_inputs():
        """This function becomes invoked when user clicks the Save button in the setup pop up location tkinter window gui."""
        global x_location 
        x_location= x_entry.get()
        global y_location
        y_location = y_entry.get()
        #save inputs into a settings file each time 
        config['SETTINGS'] = {'x_location': x_entry.get(), 
                                'y_location': y_entry.get(),}
        with open('RitualReminderPopSettings.ini', 'w') as configfile:
            config.write(configfile)

    def pop_test():
        """Displays a example pop up where the users pixel inputs were set."""
        test_window = tk.Tk()
        test_window.wm_attributes("-topmost", 1)
        test_window.title("Test")
        test_window.geometry(f"200x100+{x_entry.get()}+{y_entry.get()}")
        test_window.mainloop()


    #tk instance
    popup_setup = tk.Tk()
    popup_setup.wm_attributes("-topmost", 1)
    popup_setup.title("Ritual Reminder Pop up Settings")
    popup_setup.geometry('400x300+50+50')
    #frame inside that instance
    setup_Frame = ttk.LabelFrame(popup_setup, text='Input Locations')
    setup_Frame.pack()
    # 2 labels and input fields for values.
    popupY_label = ttk.Label(setup_Frame, text="Y value:")
    popupY_label.pack()
    y_entry = ttk.Entry(setup_Frame, width=10)
    y_entry.pack()
    y_entry.insert(tk.END, "920")
    popupX_label = ttk.Label(setup_Frame, text='X value:')
    popupX_label.pack()
    x_entry = ttk.Entry(setup_Frame, width=10)
    x_entry.pack()
    x_entry.insert(tk.END, "750")
    #Tell user what to do
    disclaimer = ttk.Label(setup_Frame, text = 'Enter where you want your popup to be on your screen. \n(These values represent the number of pixels:\n Y: From the Top of your screen down\n X:From the Left of your screen over to the right.)\n After you have entered, press Save.\nPress TEST for an empty window to show you where you will see reminders. \nYou will need to close each test window.\n\nWhen you are satisfied close the Pop up Settings window.')
    disclaimer.pack()
    #Save and Test Buttons
    save_button = ttk.Button(popup_setup, text="Save", command =lambda: save_pop_inputs())
    save_button.pack()
    test_button = ttk.Button(popup_setup, text="Test", command =lambda: pop_test())
    test_button.pack()

    #Invoke the gui loop
    popup_setup.mainloop()


# #try to open the settings file and create a variable for the Client.txt path, if client file is not named 'Client.txt', then aks user to reselect their Client.txt files location.
#Try to open the client settings file and create a variable equal to the path of your Client.txt file. If problems then
try:
    config.read('RitualReminderClientLocation.ini')
    client = config['SETTINGS']['ClientFileLocation']

#if the file doesn't exist, create it with a blank client location, then ask the user to select where the Client.txt is
except:
    config['SETTINGS'] = {'ClientFileLocation': '',}
    with open('RitualReminderClientLocation.ini', 'w') as configfile:
        config.write(configfile)
    set_client_location()
    config.read('RitualReminderClientLocation.ini')
    client = config['SETTINGS']['ClientFileLocation']

#Otherwise check if 'Client.txt' is not in the variable which is the path string. If not then ask for the selection. Otherwise try to load the popup locations of the reminder, if problems run the command to save location, otherwise run the program.
else:
    if 'Client.txt' not in client:
        set_client_location()


try:
    config.read('RitualReminderPopSettings.ini')
    x_location = config['SETTINGS']['x_location']
    y_location = config['SETTINGS']['y_location']

except:
    set_up_popup_location()
    config.read('RitualReminderPopSettings.ini')
    x_location = config['SETTINGS']['x_location']
    y_location = config['SETTINGS']['y_location']
    read_file(client)

else:
    read_file(client)