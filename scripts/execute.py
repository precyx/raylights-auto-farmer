#setup pyautogui

import pyautogui
import pyperclip
import time
import os
import datetime
import json


# load settings
SETTINGS = {}
with open("settings.json") as f:
     SETTINGS = json.load(f)

# land index
LAND_INDEX = SETTINGS["LAND_INDEX"]

# instructions

# 1. prepare the raylights app and open the console 
# 2. set the permissions on the computer to allow screenshots
# 3. use the "record.py" script to record all Positions and Areas
# 4. retake all the reference Screenshots needed for the image comparisons
# 5. set "LAND_INDEX" and "recipes" in the settings.json file
# 6. set keyboard language to english-us


# todo
# ...

# data

# constants

# UNUSED currently. amount of lands to skip until the auto farming loop starts
LAND_SCROLL_COUNT = 1; #max:300 landcount

# land base url
LAND_URL_BASE = "https://play.axieinfinity.com/raylights?land="

# axie pages
AXIE_PAGES_START_OFFSET = 200; # either 0 or 200
AXIE_PAGES_BUFFER = 0;

# Recipes
recipes = SETTINGS["recipes"]

# Mouse Positions
mouse_positions = SETTINGS['mouse_positions']

# Lands
lands = SETTINGS["lands"]

# mineral to index
mineral_to_index = SETTINGS["mineral_to_index"]

# characters
_T = "	"
_N = "\n"

# folders
INPUT_DATA_FOLDER = "data/"
INPUT_REFERENCE_IMAGE_FOLDER = "data/reference_images/"
OUTPUT_DATA_FOLDER = "output_data/execute/"
OUTPUT_IMAGES_FOLDER_NAME = "output_data/execute/output_images/"

# reference images
DISABLED_GROW_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "disabled_grow_button.png"
IS_GROWING_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "is_growing_button.png"
GO_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "go_button.png"
CLAIMABLE_WEED_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "claimable_weed.png"
CLAIM_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "claim_button.png"
ITEMS_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "items_button.png"
LAND_SELECTION_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "land_selection.png"
SETTINGS_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "settings_button.png"
CONSOLE_SETTINGS_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "console_settings.png"
CONTINUE_BUTTON_REFERENCE = INPUT_REFERENCE_IMAGE_FOLDER + "continue_button.png"

# output 
OUTPUT_IMAGES_FULL_PATH = ""
OUTPUT_LOG_FILE = "output_log.txt"
OUTPUT_RESULTS_FILE = "output_results.txt"
OUTPUT_PLANTED_FILE = "output_planted.txt"

# time
time_measure = 0;

# get screen dimensions
screen_width, screen_height = pyautogui.size()

stages = [
    "Select Land",
    "Select Minerals",
    "Select Axie",
    "Exit Land",
]

# Actions: Farm + Plant
"""
actions = [
    ["TypeUrlScript", 0.3, "script"],
    ["CheckConsoleScript", 0.3, "script"],
    ["Nursery", 0.8, "click", mouse_positions["Nursery"][0], mouse_positions["Nursery"][1]],
    ["Items", 0.8, "click", mouse_positions["Items"][0], mouse_positions["Items"][1]],
    ["CheckGrowingPlantScript", 0.3, "script"],
    ["Minerals", 0.3, "click", mouse_positions["Minerals"][0], mouse_positions["Minerals"][1]],
    ["MineralsScript", 0.3, "script"],
    ["Add Axie", 0.3, "click", mouse_positions["Add Axie"][0], mouse_positions["Add Axie"][1]],
    ["AxieScript", 0.3, "script"],
    ["Grow Button", [IS_GROWING_BUTTON_REFERENCE, 1, 90], "click", mouse_positions["Grow Button"][0], mouse_positions["Grow Button"][1]],
    ["CheckPlantedWeedScript", 0.3, "script"],
    ["IncreaseLandIndexScript", 0.1, "script"],
    ["MeasureTimeScript", 0.1, "script"],
]
""" 


# Actions: Farm only


actions = [
    ["TypeUrlScript", 0.3, "script"],
    ["CheckConsoleScript", 0.3, "script"],
    ["MiddleRightScreenClick", 0.1, "click", screen_width - 20, round(screen_height/2) - 20],
    ["Nursery", 0.8, "click", mouse_positions["Nursery"][0], mouse_positions["Nursery"][1]],
    ["Items", 0.8, "click", mouse_positions["Items"][0], mouse_positions["Items"][1]],
    ["CheckGrowingPlantScript", 0.3, "script"],
    ["IncreaseLandIndexScript", 0.1, "script"],
    ["MeasureTimeScript", 0.1, "script"],
]






# MAIN FUNCTION AutoFarm
def autoFarm():

    # - STEP #0: Setup

    global _T;
    global LAND_INDEX
    global AXIE_PAGES_BUFFER
    global AXIE_PAGES_START_OFFSET

    time.sleep(0.2);
    logOutput("\n\n\n\n" + "<--- Starting Script --->");
    logResult("\n\n" + "[" + formatTime() + "]" + " " + "<--- Starting Script --->");
    logPlanted("\n\n" + "[" + formatTime() + "]" + " " + "<--- Starting Script --->");

    logOutput(f"Trying to plant: {len(recipes)} recipes");
    logOutput(f"Starting at land index: {str(LAND_INDEX)} {str(lands[LAND_INDEX])} - going to {str(LAND_INDEX + len(recipes))} {str(lands[LAND_INDEX + len(recipes)])}");
    
    print(actions)

    # - STEP #2 - Loop through actions            

    # loop recipes
    break_recipes = False;
    for i_recipe,recipe in enumerate(recipes):

        if break_recipes:
            break

        # log completed actions
        actions_completed = []

        # loop actions 
        for action in actions:

            if break_recipes:
                break

            time.sleep(0.1)


            # ensure console is open
            console_image = CONSOLE_SETTINGS_REFERENCE
            console_location = pyautogui.locateOnScreen(console_image, confidence=0.9)

            if console_location is None:
                logOutput("Console was not found, opening console with CMD+OPT+I") 

                # press the combination OPTION + COMMAND + I with pyautogui
                # open console
                pyautogui.hotkey('option', 'command', 'i')
                time.sleep(2)

            
            # print(action[0])
            if action[2] == "click":
                pyautogui.click(action[3], action[4])
            elif action[2] == "press":
                pyautogui.press(action[3])
            elif action[2] == "doubleClick":
                pyautogui.doubleClick(action[3], action[4])
            elif action[2] == "drag":
                pyautogui.moveTo(action[3], action[4])
                pyautogui.dragTo(action[5], action[6], duration=7, button='middle')

            # test script
            if action[0] == "TestScript":
                time.sleep(1.5)
                logOutput("TEST SCRIPT")


            """
            # test axie pages script
            if action[0] == "TestAxiePagesScript":
                time.sleep(1.5)
                logOutput("TEST AXIE PAGES SCRIPT")

                break_pages = False;
                # loop 80 times max (pages loop)
                for i in range(80):

                    # click axies page #1
                    if(LAND_INDEX % 6 == 0): 
                        AXIE_PAGES_BUFFER += 3

                    x = mouse_positions["Axies Page #1"][0] + AXIE_PAGES_START_OFFSET + AXIE_PAGES_BUFFER
                    y = mouse_positions["Axies Page #1"][1]

                    print("x: " + str(x))
                    pyautogui.click(x, y)
                    time.sleep(1)
                    pyautogui.click(x, y)
                    time.sleep(1)

                    # loop 6 times (axies loop)
                    for j in range(6):

                        # click axie #1
                        label = "Axie #" + str(j + 1)
                        pyautogui.doubleClick(mouse_positions[label][0], mouse_positions[label][1])

                        time.sleep(0.5)

                    LAND_INDEX += 1
            """
                



            # type url script
            if action[0] == "TypeUrlScript":

                reload_successful = False

                # try reloading 5 times max
                for i_url in range(5):

                    if reload_successful == True:
                        break

                    # click url bar
                    url_bar_x = mouse_positions["URL Bar"][0] + 200
                    url_bar_y = mouse_positions["URL Bar"][1]

                    pyautogui.click(url_bar_x, url_bar_y, clicks=3, interval=0.15)
                    time.sleep(0.3)

                    # press backspace
                    pyautogui.press("backspace")
                    time.sleep(0.3)

                    # type land url
                    string_to_type = f'{LAND_URL_BASE}{lands[LAND_INDEX].strip()}'
                    pyautogui.typewrite(string_to_type, interval=0.01)

                    # press enter
                    pyautogui.press('enter')

                    # important sleep because of fading in screen
                    time.sleep(3)

                    image = SETTINGS_BUTTON_REFERENCE

                    running = True
                    while running == True:
                        running = sleepUntilImageFound(image, 0.9, 2, 60)
                    
                    if running == "timeout":
                        #break_recipes = True;
                        logOutput(f'TRYING_RELOADING_PAGE: Image "{image}" not found in time, trying to reload page...');
                    
                    if running == "found":
                        reload_successful = True
                    
                
                if reload_successful == False:
                    logOutput(f'ERROR_OCCURED: action:"TypeUrlScript" Image "{image}" not found in time (5 times tried), breaking the loop...');
                    break_recipes = True;

                # log entered land
                logOutput("Enter Land: " + str(lands[LAND_INDEX]) + " - " + str(LAND_INDEX))
               

            # growing plant script
            if action[0] == "CheckGrowingPlantScript":

                time.sleep(3)
                #locate on screen
                location = pyautogui.locateOnScreen(CLAIM_BUTTON_REFERENCE, confidence=0.9)

                if location is not None:
                    claim_button_x = mouse_positions["Claim Button"][0]
                    claim_button_y = mouse_positions["Claim Button"][1]
                    pyautogui.click(claim_button_x, claim_button_y)

                    image_settings = SETTINGS_BUTTON_REFERENCE
                    image_continue = CONTINUE_BUTTON_REFERENCE

                    running = True
                    while running == True:
                        running = sleepUntilImageFound([image_settings, image_continue], 1, 2, 90)
                    
                    if running == "timeout":
                        break_recipes = True;
                        logOutput(f'ERROR_OCCURED: action: "CheckGrowingPlantScript" Image "{image_settings}" and "{image_continue}" not found in time, breaking the loop...');
                    
                    print("__running " + running);

                    if(break_recipes == False):

                        # if new plant continue button is found
                        if running == "found2":

                            time.sleep(5)

                            # use * 2 because of retina display
                            x = mouse_positions["New Plant Screen TopLeft"][0] * 2;
                            y = mouse_positions["New Plant Screen TopLeft"][1] * 2;
                            width = (mouse_positions["New Plant Screen TopRight"][0] - mouse_positions["New Plant Screen TopLeft"][0])  * 2;
                            height = (mouse_positions["New Plant Screen BottomLeft"][1] - mouse_positions["New Plant Screen TopLeft"][1])  * 2;

                            # make land-screenshot
                            screenshot = pyautogui.screenshot(region=(x, y, width, height))

                            # save the land-screenshot in a folder
                            imagePath = f"{OUTPUT_IMAGES_FOLDER_NAME}/new_plant{str(LAND_INDEX)}.png"
                            screenshot.save(imagePath)

                            time.sleep(0.5)

                            # click continue button
                            pyautogui.click(mouse_positions["Continue New Plant Button"][0], mouse_positions["Continue New Plant Button"][1])

                            time.sleep(5)


                        x = mouse_positions["Console Output Line Start"][0]
                        y = mouse_positions["Console Output Line Start"][1]

                        # click the console text 2 times to select it
                        pyautogui.click(x, y)
                        time.sleep(0.1)
                        pyautogui.click(x, y)
                        time.sleep(0.1)

                        # drag right to select the text
                        pyautogui.dragTo(x + 300, y, duration=0.5, button='left')
                        
                        # right click
                        pyautogui.click(x, y, button='right')
                        time.sleep(0.5)

                        # click copy button
                        pyautogui.click(x + 30, y - 80)
                        time.sleep(0.3)

                        # click clear console button
                        console_clear_x = mouse_positions["Clear Console"][0]
                        console_clear_y = mouse_positions["Clear Console"][1]
                        pyautogui.click(console_clear_x, console_clear_y)

                        # log copied text
                        copied_result = pyperclip.paste()
                        copied_result = copied_result.replace("New plant: ", "")
                        copied_result = copied_result.replace(" ", "")

                        logResult(f'{str(LAND_INDEX)}{_T}{lands[LAND_INDEX]}{_T}{copied_result}')
                        logOutput(f'Growing Plant found: {copied_result} {str(LAND_INDEX)} {lands[LAND_INDEX]}')

                        # sleep
                        time.sleep(0.3)



            # click minerals script
            if action[0] == "MineralsScript":

                time.sleep(2)

                # loop recipe characters
                for i,character in enumerate(recipe):

                    # get mineral position
                    mineral_label = "Mineral #" + str(mineral_to_index[character]);
                    mineral_position_x = mouse_positions[mineral_label][0]
                    mineral_position_y = mouse_positions[mineral_label][1]

                    #print(str(mineral_position_x) + " " + str(mineral_position_y))
                    # click mineral
                    time.sleep(1)
                    pyautogui.doubleClick(mineral_position_x, mineral_position_y)


            # click axies script
            if action[0] == "AxieScript":

                # increase buffer all 6 lands
                if(LAND_INDEX % 6 == 0): 
                    AXIE_PAGES_BUFFER += 3

                # click axies page #1
                x = mouse_positions["Axies Page #1"][0] + round(LAND_INDEX/2) + AXIE_PAGES_START_OFFSET + AXIE_PAGES_BUFFER # calculate x offset
                y = mouse_positions["Axies Page #1"][1]
                pyautogui.click(x, y)
                time.sleep(0.5)
                pyautogui.click(x, y)
                time.sleep(0.5)


                break_pages = False;
                # loop 80 times max (pages loop)
                for i in range(80):

                    # loop 6 times (axies loop)
                    for j in range(6):

                        # click axie #1
                        label = "Axie #" + str(j + 1)
                        pyautogui.doubleClick(mouse_positions[label][0], mouse_positions[label][1])

                        # compare disabled-grow-button screenshot with reference
                        time.sleep(1)
                        location = pyautogui.locateOnScreen(DISABLED_GROW_BUTTON_REFERENCE)
                        # if there is no disabled-grow-button found 
                        # the axie was successfully selected, so break both loops and continue
                        if location == None:
                            #print("NOT FOUND")
                            break_pages = True;
                            break;

                        #print("FOUND" + str(location))
                        
                    if break_pages:
                        break;
                    else:
                        # click next page
                        pyautogui.doubleClick(mouse_positions["Next Page"][0], mouse_positions["Next Page"][1]);
                        time.sleep(0.2)


            # check planted weed script
            if action[0] == "CheckPlantedWeedScript":
                
                # compare grow button screenshot with reference
                time.sleep(0.1)
                location2 = pyautogui.locateOnScreen(IS_GROWING_BUTTON_REFERENCE)

                if location2 == None:
                    #print("NOT FOUND")
                    log = f'"{recipe}" ({i_recipe}) - RecipeIndex - ERROR_OCCURED: action:"CheckPlantedWeedScript" "Green Grow Button" was not found, plant is not growing...';
                    logOutput(log);
                    break_recipes = True;
                    break;
                else :
                    logOutput(f'"{recipe}" - RecipeIndex({i_recipe}) - LandIndex({LAND_INDEX}) [{lands[LAND_INDEX]}]');
                    logPlanted(f'{str(LAND_INDEX)}{_T}{lands[LAND_INDEX]}{_T}{recipe}');

            # drag next land script
            if action[0] == "DragNextLandScript":
                # drag next land
                success = scrollOneLandDown();
                if success == False:
                    break_recipes = True;
                    break;

            # incrase land index script
            if action[0] == "IncreaseLandIndexScript":
                LAND_INDEX += 1;

            # measure time script
            if action[0] == "MeasureTimeScript":
                logTimeDifference();



            # sleep for action time repeatedly until image is found
            if isinstance(action[1], list):

                image = action[1][0]
                sleep_time = action[1][1]
                max_time = action[1][2]

                running = True
                while running == True:
                    running = sleepUntilImageFound(image, 0.9, sleep_time, max_time)
                    print("__running: " + running)
                
                if running == "timeout":
                    break_recipes = True;
                    logOutput(f'ERROR_OCCURED: action:"{action[0]}" Image "{image}" not found in time, breaking the loop...');
                    
            # sleep for action time
            elif isinstance(action[1], int) or isinstance(action[1], float):
                time.sleep(action[1])
            
            # add completed action
            actions_completed.append(action[0])

        # log completed actions
        logOutput(f'Actions completed: {", ".join(actions_completed)}')


    # finish
    logOutput("<--- Script Finished --->");




# functions


def logOutput(value):
    print(value);
    file = open(OUTPUT_DATA_FOLDER + OUTPUT_LOG_FILE, "a")
    file.write(f'\n[{formatTime()}] {value}')
    file.close()

def logResult(value):
    print(value);
    file = open(OUTPUT_DATA_FOLDER +  OUTPUT_RESULTS_FILE, "a")
    file.write("\n" + value)
    file.close()

def logPlanted(value):
    print(value);
    file = open(OUTPUT_DATA_FOLDER +  OUTPUT_PLANTED_FILE, "a")
    file.write("\n" + value)
    file.close()


def logTimeDifference():
    global time_measure
    if time_measure != 0:
        difference = time.time() - time_measure
        difference = str(datetime.timedelta(seconds=difference))
        difference = difference.split('.')[0] # remove milliseconds
        logOutput(f'Time difference: {difference}')

    time_measure = time.time()


def formatTime():
    return time.strftime("%d/%m/%Y %H:%M:%S")

def formatTimeFolder():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def sleepUntilImageFound(image, confidence, sleep_time, max_time):

    output = ""
    start_time = time.time()


    # loop until found
    break_while = False
    while True:

        if break_while:
            break;

        # break the loop after max seconds
        if time.time() - start_time > max_time:
            output = "timeout"
            break;

        # multiple images
        if isinstance(image, list):
            for i in range(len(image)):

                location = None;
                if confidence == 1:
                    location = pyautogui.locateCenterOnScreen(image[i])
                else:
                    location = pyautogui.locateOnScreen(image[i], confidence=confidence)

                if location is not None:
                    output = "found" + str(i+1)
                    break_while = True
                    break;

        # single image
        else:
            location = None
            if confidence == 1:
                location = pyautogui.locateCenterOnScreen(image)
            else:
                location = pyautogui.locateOnScreen(image, confidence=confidence)

            # if image is found continue
            if location is not None:
                output = "found"
                break;

        time.sleep(sleep_time)

    return output



# run autoFarm function
autoFarm()
