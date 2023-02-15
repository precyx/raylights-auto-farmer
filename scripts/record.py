# setup pyautogui

import pyautogui
import time
import os

# data
mouse_positions = []
screen_width, screen_height = pyautogui.size()

# create an array with strings for the labels
labels =  [
    "URL Bar",
    "Land #1 TopLeft",
    "Land #1 TopRight",
    "Land #1 BottomLeft",
    "Land #1 BottomRight",
    "Land #1 Drag Start",
    "Land #1 Drag End",
    "Go Button Land #1",
    "Nursery",
    "Items",
    "Claim Button",
    "New Plant Screen TopLeft",
    "New Plant Screen TopRight",
    "New Plant Screen BottomLeft",
    "New Plant Screen BottomRight",
    "Continue New Plant Button",
    "Console Output Line Start",
    "Console Output Line End",
    "Clear Console",
    "Minerals",
    "Mineral #1",
    "Mineral #2",
    "Mineral #3",
    "Mineral #4",
    "Mineral #5",
    "Mineral #6",
    "Mineral #7",
    "Mineral #8",
    "Mineral #9",
    "Mineral #10",
    "Mineral #11",
    "Mineral #12",
    "Disabled Grow Button TopLeft",
    "Disabled Grow Button TopRight",
    "Disabled Grow Button BottomLeft",
    "Disabled Grow Button BottomRight",
    "Add Axie",
    "Axies Page #1",
    "Axies Pages 50%",
    "Axie #1",
    "Axie #2",
    "Axie #3",
    "Axie #4",
    "Axie #5",
    "Axie #6",
    "Next Page",
    "Grow Button",
    "Close Nursery",
    "Settings Button",
    "Lands Button",
]

# create a loop with the labels array and the above code
for label in labels:
    input('Move the Mouse to: ' + label)
    mouse_x, mouse_y = pyautogui.position()
    mouse_positions.append([label, mouse_x, mouse_y])
    print(label + ': ' + str(mouse_x) + ', ' + str(mouse_y))


print(mouse_positions)

# save the array to a file
with open('output_data/record/mouse_positions.txt', 'w') as f:
    for item in mouse_positions:
        f.write("" + "'" + str(item[0]) + "'" + ":" + "[" + str(item[1])  + "," + str(item[2]) + "]," + "\n")
            

# save the array to a file
with open('output_data/record/mineral_positions.txt', 'w') as f:       
    for item in mouse_positions:
        # write if item[0] conatins "Mineral ":
        if("Mineral " in item[0]):
            f.write("" + "'" + str(item[0]) + "'" + ":" + "[" + str(item[1])  + "," + str(item[2]) + "]," + "\n")


