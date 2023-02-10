#setup pyautogui

import pyautogui
import pyperclip
import time
import os
import datetime


# settings

# land index
LAND_INDEX = 0;

# instructions

# 1. prepare the raylights app and open the console 
# 2. set the permissions on the computer to allow screenshots
# 3. use the "record.py" script to record all Positions and Areas
# 4. retake all the reference Screenshots needed for the image comparisons
# 5. set "LANDLIST_ITEM_HEIGHT" manually to the height of one land list item (todo: make dynamic)
# 6. set "LAND_SCROLL_COUNT" to the amount of lands to skip 
# 7 set "LAND_INDEX" to the index of the first land you want to farm
# 8. set the Lands array to the lands you own
# 9. set the Recipes array to the recipes you want to farm
# 10. set keyboard language to english-us


# todo

# - [OK] output results into new txt
# - improve performance x2

# data

# constants

# UNUSED currently. amount of lands to skip until the auto farming loop starts
LAND_SCROLL_COUNT = 1; #max:300 landcount

# ui land list item height
LANDLIST_ITEM_HEIGHT = 43; # std:60 # todo: make this value calculated / recorded
LANDLIST_INITIAL_HEIGHT = None;
LANDLIST_SCROLL_CORRECTION = None;
LAND_URL_BASE = "https://play.axieinfinity.com/raylights?land="

# axie pages
AXIE_PAGES_START_OFFSET = 200; # either 0 or 200
AXIE_PAGES_BUFFER = 0;

# characters
_T = "	"
_N = "\n"

# reference images
reference_image_folder = "reference_images/"
DISABLED_GROW_BUTTON_REFERENCE = reference_image_folder + "disabled_grow_button.png"
IS_GROWING_BUTTON_REFERENCE = reference_image_folder + "is_growing_button.png"
GO_BUTTON_REFERENCE = reference_image_folder + "go_button.png"
CLAIMABLE_WEED_REFERENCE = reference_image_folder + "claimable_weed.png"
CLAIM_BUTTON_REFERENCE = reference_image_folder + "claim_button.png"
ITEMS_BUTTON_REFERENCE = reference_image_folder + "items_button.png"
LAND_SELECTION_REFERENCE = reference_image_folder + "land_selection.png"
SETTINGS_BUTTON_REFERENCE = reference_image_folder + "settings_button.png"

# output 
OUTPUT_IMAGES_FOLDER_NAME = "output_images"
OUTPUT_IMAGES_FULL_PATH = ""
OUTPUT_LOG_FILE = "output_log.txt"
OUTPUT_RESULTS_FILE = "output_results.txt"
OUTPUT_PLANTED_FILE = "output_planted.txt"

# time
time_measure = 0;

# get screen dimensions
screen_width, screen_height = pyautogui.size()

# Recipes
recipes = [
    "001",
    "002",
    "003",
    "004",
    "005",
    "006",
    "007",
    "008",
    "009",
    "010",
    "011",
    "012",
    "013",
    "014",
    "015",
    "016",
    "017",
    "018",
    "019",
    "020",
    "021",
    "022",
    "023",
    "024",
    "025",
    "026",
    "027",
    "028",
    "029",
    "030",
    "031",
    "032",
    "033",
    "034",
    "035",
    "036",
    "037",
    "038",
    "039",
    "040",
    "041",
    "042",
    "043",
    "044",
    "045",
    "046",
    "047",
    "048",
    "049",
    "050",
    "051",
    "052",
    "053",
    "054",
    "055",
    "056",
    "057",
    "058",
    "059",
    "060",
    "061",
    "062",
    "063",
    "064",
    "065",
    "066",
    "067",
    "068",
    "069",
    "070",
    "071",
    "072",
    "073",
    "074",
    "075",
    "076",
    "077",
    "078",
    "079",
    "080",
    "081",
    "082",
    "083",
    "084",
    "085",
    "086",
    "087",
    "088",
    "089",
    "090",
    "091",
    "092",
    "093",
    "094",
    "095",
    "096",
    "097",
    "098",
    "099",
    "100",
    "101",
    "102",
    "103",
    "104",
    "105",
    "106",
    "107",
    "108",
    "109",
    "110"
]

stages = [
    "Select Land",
    "Select Minerals",
    "Select Axie",
    "Exit Land",
]


mouse_positions = {
    'URL Bar':[407,86],
    'Land #1 TopLeft':[298,340],
    'Land #1 TopRight':[761,341],
    'Land #1 BottomLeft':[297,398],
    'Land #1 BottomRight':[763,399],
    'Land #1 Drag Start':[516,363],
    'Land #1 Drag End':[523,298],
    'Go Button Land #1':[713,368],
    'Nursery':[93,231],
    'Items':[32,231],
    'Claim Button':[1275,599],
    'Console Output Line Start':[12,856],
    'Console Output Line End':[438,855],
    'Clear Console':[44,793],
    'Minerals':[103,297],
    'Mineral #1':[57,375],
    'Mineral #2':[124,380],
    'Mineral #3':[188,377],
    'Mineral #4':[252,377],
    'Mineral #5':[318,375],
    'Mineral #6':[385,379],
    'Mineral #7':[60,443],
    'Mineral #8':[123,448],
    'Mineral #9':[190,446],
    'Mineral #10':[257,449],
    'Mineral #11':[316,446],
    'Mineral #12':[388,447],
    'Disabled Grow Button TopLeft':[1213,259],
    'Disabled Grow Button TopRight':[1424,260],
    'Disabled Grow Button BottomLeft':[1216,353],
    'Disabled Grow Button BottomRight':[1427,359],
    'Add Axie':[1278,678],
    'Axies Page #1': [72,659],
    'Axies Pages 50%' : [272,659],
    'Axie #1':[119,424],
    'Axie #2':[281,422],
    'Axie #3':[453,422],
    'Axie #4':[107,568],
    'Axie #5':[283,572],
    'Axie #6':[446,573],
    'Next Page':[497,659],
    'Grow Button':[1315,311],
    'Close Nursery':[93,234],
    'Settings Button':[1404,227],
    'Lands Button':[1088,402]
}

mineral_to_index = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 10,
    "A": 11,
    "B": 12,
}

# todo: map weed to classifications
weed_to_classification = {
    "moss_01": "Withering",
    "moss_02": "Withering",
}

lands = [
    "-82,-117",
    "-67,0",
    "-132,-92",
    "-53,20",
    "-53,19",
    "-53,-7",
    "-54,20",
    "-54,19",
    "-54,18",
    "-55,20",
    "-55,19",
    "-56,20",
    "-65,2",
    "-65,1",
    "-65,0",
    "-65,-1",
    "-66,2",
    "-66,1",
    "-66,0",
    "-66,-1",
    "-67,3",
    "-67,1",
    "-67,-1",
    "-68,3",
    "-68,2",
    "-68,1",
    "-68,0",
    "-68,-1",
    "-69,3",
    "-69,2",
    "-69,1",
    "-69,0",
    "-69,-1",
    "-101,-44",
    "-101,-45",
    "-101,-46",
    "-101,-47",
    "-101,-48",
    "-101,-49",
    "-102,-43",
    "-102,-45",
    "-102,-47",
    "-102,-48",
    "-101,-60",
    "-103,-42",
    "-103,-43",
    "-103,-44",
    "-103,-45",
    "-103,-48",
    "-103,-49",
    "-104,-42",
    "-104,-43",
    "-104,-49",
    "-104,-59",
    "-105,27",
    "-105,-41",
    "-105,-42",
    "-105,-43",
    "-105,-44",
    "-106,-42",
    "-106,-44",
    "-109,-86",
    "-115,-2",
    "-82,17",
    "-112,-2",
    "-76,-97",
    "-52,19",
    "-52,20",
    "-50,-55",
    "-50,-54",
    "-112,-3",
    "-86,7",
    "-49,-57",
    "-49,-56",
    "-49,-55",
    "-49,-54",
    "-92,-26",
    "-85,-110",
    "-83,17",
    "-48,-76",
    "-48,-56",
    "-48,-55",
    "-48,-54",
    "-92,-25",
    "-112,-1",
    "-83,18",
    "-87,-65",
    "-83,16",
    "-83,19",
    "-87,-44",
    "-101,29",
    "-101,-43",
    "-39,-132",
    "-38,-133",
    "-38,-132",
    "-38,-131",
    "-38,-130",
    "-37,-125",
    "-37,-103",
    "-36,-104",
    "-36,-103",
    "-36,-102",
    "-36,-101",
    "-35,-105",
    "-35,-104",
    "-35,-103",
    "-35,-102",
    "-35,-101",
    "-34,-105",
    "-34,-104",
    "-34,-103",
    "-34,-102",
    "-33,-106",
    "-33,-105",
    "-33,-104",
    "-33,-103",
    "-33,-102",
    "-33,-101",
    "-149,-99",
    "-147,-98",
    "-144,-55",
    "-144,-22",
    "-140,-19",
    "-140,-14",
    "-140,-13",
    "-139,-86",
    "-139,-85",
    "-139,-13",
    "-138,-87",
    "-138,-86",
    "-138,-85",
    "-138,-84",
    "-138,-60",
    "-137,-88",
    "-137,-87",
    "-137,-86",
    "-137,-85",
    "-137,-84",
    "-137,-83",
    "-136,-90",
    "-136,-89",
    "-136,-88",
    "-136,-87",
    "-136,-86",
    "-136,-85",
    "-136,-84",
    "-136,-83",
    "-136,-82",
    "-136,-42",
    "-136,-41",
    "-135,-91",
    "-135,-90",
    "-135,-89",
    "-135,-88",
    "-135,-87",
    "-135,-86",
    "-135,-85",
    "-135,-84",
    "-135,-83",
    "-135,-82",
    "-134,-92",
    "-134,-91",
    "-134,-90",
    "-134,-89",
    "-134,-88",
    "-134,-87",
    "-134,-86",
    "-134,-85",
    "-134,-84",
    "-134,-83",
    "-134,-82",
    "-133,-93",
    "-133,-92",
    "-133,-91",
    "-133,-90",
    "-133,-89",
    "-133,-88",
    "-133,-87",
    "-133,-86",
    "-133,-85",
    "-133,-84",
    "-133,-83",
    "-133,-82",
    "-133,-83",
    "-133,-82",
    "-82,18",
    "-132,-91",
    "-132,-90",
    "-132,-89",
    "-132,-88",
    "-132,-87",
    "-132,-86",
    "-132,-85",
    "-132,-84",
    "-132,-83",
    "-132,-82",
    "-131,-91",
    "-131,-90",
    "-131,-89",
    "-131,-88",
    "-131,-87",
    "-131,-86",
    "-131,-85 ",
    "-131,-84",
    "-131,-83",
    "-131,-82",
    "-130,-90",
    "-130,-89",
    "-130,-88",
    "-130,-87",
    "-130,-86",
    "-130,-85",
    "-130,-84",
    "-130,-83",
    "-130,-82",
    "-129,-89",
    "-129,-88",
    "-129,-87",
    "-129,-86",
    "-129,-85",
    "-129,-84",
    "-129,-83",
    "-129,-4",
    "-129,-3",
    "-129,-1",
    "-129,0",
    "-128,-88",
    "-128,-87",
    "-128,-86",
    "-128,-85",
    "-128,-84",
    "-128,-1",
    "-128,1",
    "-128,3",
    "-127,-87",
    "-127,-86",
    "-127,-85",
    "-127,-7",
    "-127,-3",
    "-127,-2",
    "-127,0",
    "-127,1",
    "-127,2",
    "-127,8",
    "-126,-86",
    "-126,-7",
    "-126,-3",
    "-126,-1",
    "-126,2",
    "-126,3",
    "-126,4",
    "-126,5",
    "-125,-86",
    "-125,-5",
    "-125,-4",
    "-125,-3",
    "-125,4",
    "-124,-97",
    "-124,-82",
    "-124,-5",
    "-124,-4",
    "-124,2",
    "-124,3",
    "-124,5",
    "-123,-5",
    "-123,-4",
    "-122,-8",
    "-122,2",
    "-122,3",
    "-122,4",
    "-121,6",
    "-121,8",
    "-120,5",
    "-120,7",
    "-120,8",
    "-119,-143",
    "-119,-9",
    "-119,-8",
    "-119,-7",
    "-119,-6",
    "-119,-5",
    "-119,-4",
    "-119,-3",
    "-119,-2",
    "-119,2",
    "-119,3",
    "-119,4",
    "-119,5",
    "-119,6",
    "-118,-9",
    "-118,-8",
    "-118,-7",
    "-118,-5",
    "-118,-4",
    "-118,-3",
    "-118,-2",
    "-118,3",
    "-118,4",
    "-118,5",
    "-118,9",
    "-118,28",
    "-117,-9",
    "-117,-8",
    "-117,-7",
    "-117,-6",
    "-117,-5",
    "-117,-3",
    "-117,-2",
    "-117,4",
    "-117,5",
    "-117,6",
    "-117,9",
    "-116,-9",
    "-116,-8",
    "-116,-7",
    "-116,-6",
    "-116,-5",
    "-116,-2",
    "-116,6",
    "-116,7",
    "-115,-85",
    "-115,-9",
    "-115,-8",
    "-115,-7",
    "-115,-6",
    "-115,7",
    "-114,-9",
    "-114,-8",
    "-114,-7",
    "-114,1",
    "-114,6",
    "-114,7",
    "-113,-9",
]

actions = [
    ["TypeUrlScript", 0.3, "script"],
        ####---["MiddleRightScreenClick", 0.1, "click", screen_width - 20, round(screen_height/2) - 20],
        ####---["TestScript", 0.4, "script"],
        ####---["URL Bar", 1.5, "click", mouse_positions["URL Bar"][0], mouse_positions["URL Bar"][1]],
        ####---["Press Enter", 16, "press", "enter"],
        ####---["Go Button Land #1", 0.3, "click", mouse_positions["Go Button Land #1"][0], mouse_positions["Go Button Land #1"][1]],
        ####---["Go Button Land #1", [ITEMS_BUTTON_REFERENCE, 1, 60], "click", mouse_positions["Go Button Land #1"][0], mouse_positions["Go Button Land #1"][1]],
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
        ####---["Nursery", 0.8, "click", mouse_positions["Nursery"][0], mouse_positions["Nursery"][1]],
        ####---["Settings Button", 0.8, "click", mouse_positions["Settings Button"][0], mouse_positions["Settings Button"][1]],
        ####---["Lands Button", [LAND_SELECTION_REFERENCE, 1, 90], "click", mouse_positions["Lands Button"][0], mouse_positions["Lands Button"][1]],
        ####---["DragNextLandScript", 0.3, "script"],
]

# only check the plants, dont plant anything
actions = [
    ["TypeUrlScript", 0.3, "script"],
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
    global OUTPUT_IMAGES_FULL_PATH

    time.sleep(0.2);
    logOutput("\n\n" + "<--- Starting Script --->");
    logResult("\n\n" + "[" + formatTime() + "]" + " " + "<--- Starting Script --->");
    logPlanted("\n\n" + "[" + formatTime() + "]" + " " + "<--- Starting Script --->");
    
    print(actions)

    # create folder inside folder "output_images" with the current date and time using the formatTimeFolder function
    OUTPUT_IMAGES_FULL_PATH = OUTPUT_IMAGES_FOLDER_NAME + "/" + formatTimeFolder();
    os.mkdir(OUTPUT_IMAGES_FULL_PATH);
    logOutput("output folder: " + OUTPUT_IMAGES_FULL_PATH);


    # - STEP #1: Scroll to desired land position
    #success = scrollToLandPosition();
    #if success == False:
    #    return False;


    # - STEP #2 - Loop through actions            

    global LAND_INDEX
    global AXIE_PAGES_BUFFER
    global AXIE_PAGES_START_OFFSET

    # loop recipes
    break_recipes = False;
    for i_recipe,recipe in enumerate(recipes[LAND_INDEX:]): # slice by land index

        if break_recipes:
            break

        # loop actions 
        for action in actions:

            if break_recipes:
                break

            time.sleep(0.1)
            
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
                logOutput("Enter Land: " + lands[LAND_INDEX] + " - " + LAND_INDEX)

                

            # growing plant script
            if action[0] == "CheckGrowingPlantScript":

                time.sleep(3)
                #locate on screen
                location = pyautogui.locateOnScreen(CLAIMABLE_WEED_REFERENCE, confidence=0.9)

                if location is not None:
                    claim_button_x = mouse_positions["Claim Button"][0]
                    claim_button_y = mouse_positions["Claim Button"][1]
                    pyautogui.click(claim_button_x, claim_button_y)

                    image = SETTINGS_BUTTON_REFERENCE

                    running = True
                    while running == True:
                        running = sleepUntilImageFound(image, 0.9, 2, 90)
                    
                    if running == "timeout":
                        break_recipes = True;
                        logOutput(f'ERROR_OCCURED: action:"CheckGrowingPlantScript" Image "{image}" not found in time, breaking the loop...');
                    
                    if(break_recipes == False):

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

                        logResult(f'{lands[LAND_INDEX]}{_T}{copied_result}{_T}{LAND_INDEX}')
                        logOutput(f'Growing Plant found: {lands[LAND_INDEX]} {copied_result} {LAND_INDEX}')

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
                x = mouse_positions["Axies Page #1"][0] + AXIE_PAGES_START_OFFSET + AXIE_PAGES_BUFFER # calculate x offset
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
                    logPlanted(f'{lands[LAND_INDEX]}{_T}{recipe}{_T}{LAND_INDEX}');

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




    # finish
    logOutput("<--- Script Finished --->");




# functions


def scrollToLandPosition():

    global LAND_INDEX;

    # log
    logOutput("Scrolling to land index: " + str(LAND_INDEX));
    logResult("Scrolling to land index: " + str(LAND_INDEX));

    scrollDownSuccess = True

     # loop max 300 times
    for i in range(LAND_SCROLL_COUNT):

        scrollDownFail = scrollOneLandDown();
        if scrollDownFail == False:
            break;
    
    return scrollDownFail;


def scrollOneLandDown():

    global LANDLIST_SCROLL_CORRECTION
    global LANDLIST_INITIAL_HEIGHT
    global LAND_INDEX
    global OUTPUT_IMAGES_FOLDER_NAME

    # calculate drag range y
    drag_range_y = LANDLIST_ITEM_HEIGHT - (LANDLIST_SCROLL_CORRECTION or 0);
    LAND_LIST_SCROLL_CORRECTION = 0;

    # move mouse to the position specified
    pyautogui.moveTo(
        mouse_positions["Land #1 Drag Start"][0], 
        mouse_positions["Land #1 Drag Start"][1]
    )
    # drag mouse to the position specified
    pyautogui.dragTo(
        mouse_positions["Land #1 Drag End"][0], 
        mouse_positions["Land #1 Drag Start"][1] - drag_range_y, 
        duration=4,  #std-duration: 4
        button='middle'
    )

    # sleep
    time.sleep(1); #std:3

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
    imagePath = f"{OUTPUT_IMAGES_FULL_PATH}/land_{LAND_INDEX} {formatTimeFolder()}.png"
    land_screenshot.save(imagePath)

    # locate go button on screen, use *2 because of retina display
    location = pyautogui.locateOnScreen(
        GO_BUTTON_REFERENCE, 
        region=(land_1_area_x, land_1_area_y, land_1_area_width, land_1_area_height), 
        confidence=0.9
    )

    # if go button image is not found, exit program
    if location is None:
        logOutput("ERROR - Could not locate GO_BUTTON_REFERENCE image, likely because of incorrect scrolling-y correction")
        return False

    # if got button image is found, calculate correction value
    else:
        if LANDLIST_INITIAL_HEIGHT is None:
            LANDLIST_INITIAL_HEIGHT = location.top;

        # difference of initial height and current height. divide by 2 to reduce jitter
        LANDLIST_SCROLL_CORRECTION = round((LANDLIST_INITIAL_HEIGHT - location.top) / 2);
        logOutput("SCROLL_CORRECTION_Y: " + str(LANDLIST_SCROLL_CORRECTION));

    # increment land index
    LAND_INDEX += 1

    # output location and index
    logOutput(f'LandIndex({LAND_INDEX})');
    logOutput(f'Land Location: {location}');


    return True;



def logOutput(value):
    print(value);
    file = open(OUTPUT_LOG_FILE, "a")
    file.write(f'\n[{formatTime()}] {value}')
    file.close()

def logResult(value):
    print(value);
    file = open(OUTPUT_RESULTS_FILE, "a")
    file.write("\n" + value)
    file.close()

def logPlanted(value):
    print(value);
    file = open(OUTPUT_PLANTED_FILE, "a")
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
    while True:
        # break the loop after max seconds
        if time.time() - start_time > max_time:
            output = "timeout"
            break;

        location = pyautogui.locateOnScreen(image, confidence=confidence)

        # if image is found continue
        if location is not None:
            output = "found"
            break;

        time.sleep(sleep_time)

    return output



# run autoFarm function
autoFarm()


