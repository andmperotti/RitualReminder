# RitualReminder
A python script that reads the client.txt file of Path of exile and alerts users when they interact with a Ritual in the game via a lightweight tkinter gui popup. 

<img src="https://i.imgur.com/9rokc1S.jpg">

Requires Python installation. 

https://www.python.org/
https://i.imgur.com/vsYRM5J.png

add to path
https://i.imgur.com/zzgJElV.png

For selecting your client file:
For Steam Users:
C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\
is where you'd find your Client.txt file if you defaulted to normal pathing when downloading

For Standalone (pathofexile.com downloader) client file:
C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs
is where you'd find your Client.txt file if you defaulted to normal pathing when downloading

To change where the pop up occurs:
< img src="https://i.imgur.com/OXPNdct.png">
change these value, the first represents the X version, how many pixels from the left of your screen the top left corner of the pop up will be placed at. The seconf value being the Y value, which is how many pixels down from the top of the screen the popup window will be at.

When you open the script it will run in a command prompt window, you need to keep that open and running. While running each time you click on a ritual in game it will create a print out in that command prompt window telling you what time you interacted with a ritual.


Disclaimer: This is my first programming project, and I will work on it when I have time to. Apologies for any delays.

#Mapwatch has added a ritual reminder after I brought to light "FindClosestObject" was being inserted into the client.txt, I highly recommend using his app/tool as it has many useful other functions! https://github.com/mapwatch/mapwatch


Final note, please go ahead and yoink this code if you can make it better, as long as it helps the POE community then I'm all for it!

12/6/2021 Update: Removed first version for a more lightweight edition.
