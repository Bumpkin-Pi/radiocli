from os import system
import inquirer
from stations import *

def play(url):
	print("Playing radio with mpv... ")
	system("mpv "+url) # This program would probably be better suited to sh, but I want it to work on windows without much effort.

# print(stations)

catagory = stations[inquirer.prompt([
    inquirer.List(
        "catagory",
        message="Select catagory",
        choices=stations.keys(),
    ),
])["catagory"]]

station = catagory[inquirer.prompt([
    inquirer.List(
        "station",
        message="Select station",
        choices=catagory.keys(),
    ),
])["station"]]

play(station)

# answers = 
# print(answers)