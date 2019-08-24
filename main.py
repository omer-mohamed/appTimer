from win32gui import GetWindowText, GetForegroundWindow
from os import system
import time
from activity import *
import json
import csv
import json
from pandas.io.json import json_normalize

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = AcitivyList([])
first_time = True

def toTable():

    with open('activities.json') as data_file:
        data = json.load(data_file)
    print(json_normalize(data))


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
            new_window_name = window[:hifen_position[0]]

        elif hifen_counter == 0:
            new_window_name = window
        else:
            size = len(hifen_position)
            new_window_name = window[hifen_position[size-2]:hifen_position[size-1]]
            new_window_name = new_window_name[2:]


        if active_window_name != new_window_name:
            print(active_window_name)
            activity_name = active_window_name

            if not first_time:
                end_time = datetime.datetime.now()
                time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
                time_entry._get_specific_times()

                exists = False
                for activity in activeList.activities:
                    if activity.name == activity_name:
                        exists = True
                        activity.time_entries.append(time_entry)

                if not exists:
                    activity = Activity(activity_name, [time_entry])
                    activeList.activities.append(activity)
                with open('activities.json', 'w') as json_file:
                    json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
                    start_time = datetime.datetime.now()
            first_time = False
            active_window_name = new_window_name


        time.sleep(8)
except KeyboardInterrupt:
    with open('activities.json', 'w') as json_file:
        json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
    toTable()
