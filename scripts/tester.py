# setup pyautogui

import pyautogui
import time
import os

# data
mouse_positions = []
screen_width, screen_height = pyautogui.size()

# create an array with strings for the labels
labels =  [
    "Coordinate #1",
    "Coordinate #2",
    "Coordinate #3",
    "Coordinate #4",
]

print("Screensize: " + str(pyautogui.size()))

# create a loop with the labels array and the above code
for label in labels:
    input('Move the Mouse to: ' + label)
    mouse_x, mouse_y = pyautogui.position()
    mouse_positions.append([label, mouse_x, mouse_y])
    print(label + ': ' + str(mouse_x) + ', ' + str(mouse_y))


print(mouse_positions)

# save the array to a file
with open('tester.txt', 'w') as f:
    for item in mouse_positions:
        f.write("" + "'" + str(item[0]) + "'" + ":" + "[" + str(item[1])  + "," + str(item[2]) + "]," + "\n")
            
