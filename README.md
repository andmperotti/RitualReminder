Edit: As of 12/24/2022 it seems as if GGG has fixed the interaction with clicking on a ritual encounter and it proccing the text line in the client file resulting in terminating the functionality of this program :(


# RitualReminder

As of 3.17 When entering Karui Shores, there are errors that proc the "FIndClosestObject" wording in the client.txt... nothing I can do about that.


A python script that reads the client.txt file of Path of exile and alerts users when they interact with a Ritual in the game via a lightweight tkinter gui popup. 

video walkthrough: 
https://www.twitch.tv/videos/1286822982



<img src="https://i.imgur.com/9rokc1S.jpg">

Requires Python installation. 

https://www.python.org/

<img src="https://i.imgur.com/vsYRM5J.png">

add to path

<img src="https://i.imgur.com/zzgJElV.png">

After installing python, run command prompt (type "cmd" without the quotes into the box that comes up after pressing the windows key and the R key at the same time. Then type this: pip install datetime

That will install a library of code for python to log in the terminal window while ritualReminder runs to log times of when you clicked on ritual.


FOR THE RITUAL REMINDER FILE:

On the right side of your screen there is a release section:

CLICK ON "Lightweight Version Finalized Latest"

Scroll down to the "Source code (zip)", download that

unzip the file and find the "RitualReminder.py" file, put that where ever you want.





For selecting your client file:
For Steam Users:
C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\
is where you'd find your Client.txt file if you defaulted to normal pathing when downloading

For Standalone (pathofexile.com downloader) client file:
C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs
is where you'd find your Client.txt file if you defaulted to normal pathing when downloading

To change where the pop up occurs:
<img src="https://i.imgur.com/OXPNdct.png">
change these values, the first represents the X value (how many pixels from the left of your screen the top left corner of the pop up will be placed at). The second value being the Y value (which is how many pixels down from the top of the screen the popup window will be at).

When you open the script it will run in a command prompt window, you need to keep that open and running. While running each time you click on a ritual in game it will create a print out in that command prompt window telling you what time you interacted with a ritual.




Disclaimer: This was my first programming project, and I will work on it when I have time to. Apologies for any delays.

#Mapwatch has added a ritual reminder after I brought to light that "FindClosestObject" was being inserted into the client.txt, I highly recommend using his app/tool as it has many useful other functions! https://github.com/mapwatch/mapwatch 


Final note, please go ahead and yoink this code if you can make it better, as long as it helps the POE community then I'm all for it!

12/6/2021 Update: Removed first version for a more lightweight edition.

2/4/2022 Update: Restructured this page to show images and explained in detail how to install datetime module.
