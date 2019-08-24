from win32gui import GetWindowText, GetForegroundWindow
from os import system
import time
from activity import *
import json
import datetime

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = AcitivyList([])
first_time = True

try:
    while True:
        hifen_counter = 0
        hifen_position =[]
        window = GetWindowText(GetForegroundWindow())

        for i, char in enumerate(window):
            if char == "-":
                hifen_counter+=1
                hifen_position.append(i);

        if hifen_counter == 1:
            active_name = window[:hifen_position[0]]

        elif hifen_counter == 0:
            active_name = window
        else:
            print(hifen_counter)
            print(window)
            size = len(hifen_position)
            active_name = window[hifen_position[size-2]:hifen_position[size-1]]
            active_name = active_name[2:]
        print(active_name)


        time.sleep(6)
except KeyboardInterrupt:"""
    with open('activities.json', 'w') as json_file:
        json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
"""
