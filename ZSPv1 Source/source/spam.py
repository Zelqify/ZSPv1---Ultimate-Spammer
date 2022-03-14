from gevent import config
import pyautogui, time
import json





config_file = open("config.json")
json_data = json.load(config_file)

while True:
  
   

    
    if json_data["KeyBindedChat"] == True:
        pyautogui.press(json_data["KeyToOpenChat"])



    pyautogui.typewrite(json_data["TextObject"])
    pyautogui.press("enter")
    time.sleep(json_data["Duration"])
       

