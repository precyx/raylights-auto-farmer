import pyautogui
import pyperclip
import time
import os
import datetime 

FOLDER = ""

mouse_positions = {
    'Land #1 TopLeft':[298,340],
    'Land #1 TopRight':[761,341],
    'Land #1 BottomLeft':[297,398],
    'Land #1 BottomRight':[763,399],
}


# use * 2 because of retina display
land_1_area_x = mouse_positions["Land #1 TopLeft"][0] * 2;
land_1_area_y = mouse_positions["Land #1 TopLeft"][1] * 2;
land_1_area_width = (mouse_positions["Land #1 TopRight"][0] - mouse_positions["Land #1 TopLeft"][0])  * 2;
land_1_area_height = (mouse_positions["Land #1 BottomLeft"][1] - mouse_positions["Land #1 TopLeft"][1])  * 2;

# make land-screenshot
land_screenshot = pyautogui.screenshot(
    region=(land_1_area_x, land_1_area_y, land_1_area_width, land_1_area_height)
)

# save the land-screenshot in a folder
imagePath = f"land_screenshot_1.png"
land_screenshot.save(imagePath)

print("Done! - land_screenshot_1.png")