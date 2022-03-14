import math
import os
import json

print("Welcome to ZSPv1.\n\n[start] to start.\n[options] for options.")

answer1 = input(">> ")


if answer1 == "start":
    os.system("cls")
    print("ZSPv1 successfully started.\nClose the terminal to shut it off.")
    os.system("spam.py")
elif answer1 == "options":
    os.system("cls")
    print("OPTIONS:\n\n[1] to change text.\n\n[2] to change duration\n\n\n")
    
    answer2 = input(">> ")

    if answer2 == "1":
        os.system("cls")
        answer3 = input("Set text: ")

        a_file = open("config.json", "r")
        json_object = json.load(a_file)
        a_file.close()


        json_object["TextObject"] = answer3

        a_file = open("config.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
    elif answer2 == "2":
        os.system("cls")
        answer3 = int(input("Set duration (secs): "))

        a_file = open("config.json", "r")
        json_object = json.load(a_file)
        a_file.close()


        json_object["Duration"] = answer3

        a_file = open("config.json", "w")
        json.dump(json_object, a_file)
        a_file.close()

