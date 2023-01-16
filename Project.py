### Instructions for 'project'
# In python✅
# 'main()' function✅
# Minimum: 3 other functions, or more✅
# Test the code with test_project.py, any testing of function should be called test_samefname✅
# Any pip install library, to be listed in requirements.txt✅
### Submission instructions
# Video ~3min, slides, screenshots, voiceover to explain the project; then upload it to YouTube✅
# README.md file in project.py folder, to explain the project with details (markdown)✅
# submit50 cs50/problems/2022/python/project✅
"""
*** The dog is hungry - documentation ***

dictionary breeds: list of breeds of dog and related daily amount of food (can be expanded and modified)
dictionary weights: list of possible weights of dog and related daily amount of food (can be expanded and modified)

> Input
param animal_type: the user is prompted to type the type of pet (e.g. dog, cat, mouse etc)
type animal_type: str
param dog_type: the user is prompted to type the breed of the dog (e.g. Golden retriever, Bulldog etc)
type dog_type: str, transformed into capitlized str (to match the key values in the breeds dict)
param dog_weight: the user is prompted to type the weight of the dog
type dog_weight: int
param dog_name: the user is prompted to type the name of the dog
type dog_name: str
param feeding_hours: the user is prompted to type the hours when the dog should be fed. Please separate the hour times with ', '.
                     (e.g. 08:30, 13:30 or 08:30 AM, 04:30 PM etc)
type feeding_hours: str, or list of str if >1 elements
param food_amount: if no breed nor weight is given, then the amount of food must be inserted manually
type food_amount: int

> Functions
function pet_type: checks if the input pet is "dog" (case insensitive), otherwise the program ends, parameter: animal_type
function time_feeding: splits the input str (feeding hours) into the different str hours.
                       checks each str split for the correct format (with regex); transforms each split into datetime format; appends each split
                       to the list (feeding_hours_list)
                       param: feeding_hours
                       correct format of hour to input: hh:mm, hh:mm, hh:mm OR hh:mm AM|PM, hh:mm AM|PM atc
                       param n: lenght of the returned list with hours by time_feeding function
function breed_food: goes through the dictionary with dog breeds and related food amount, to find the correspendent amount
                     param: dog_type
function dog_weight_modulo: rounds the input dog weight to the nearest multiple of 5
                            param: dog_weight
function weight_food: goes through the dictionary with dog weights and related food amount, to find the correspendent amount
                      param: dog_weight
function dog_is_hungry: gets the current time; checks if the current time corresponds to the settled times, only then print out the amoung of food;
                        otherwise exits and say that it's not the right hour
                        param: food_amount, feeding_hours_list, dog_name, n
"""
import re
import sys
from datetime import datetime
import pytz

breeds = [
    {"breed" : "Golden retriever", "food" : 700},
    {"breed" : "Newfoundland", "food" : 900},
    {"breed" : "Labrador retriever", "food" : 700},
    {"breed" : "Border collie", "food" : 500},
    {"breed" : "Australian sheperd", "food" : 600},
    {"breed" : "Yorkshire", "food" : 100},
    {"breed" : "Bulldog", "food" : 300},
    {"breed" : "Bernese mountain", "food" : 900}
]

weights = [
    {"weight" : 45, "food" : 900},
    {"weight" : 40, "food" : 800},
    {"weight" : 35, "food" : 700},
    {"weight" : 30, "food" : 600},
    {"weight" : 25, "food" : 500},
    {"weight" : 20, "food" : 400},
    {"weight" : 15, "food" : 300},
    {"weight" : 10, "food" : 200},
    {"weight" : 5, "food" : 100}
]


def main():
    for i in breeds:
        print(f"{i['breed']}")
    for i in weights:
        print(f"{i['weight']}")

    print("Settings of the automatic feeding dispenser:")

    animal_type = input("Pet type: ")

    pet_type(animal_type.lower())

    dog_type = input("Dog's breed: ").capitalize()

    dog_weight = input("Dog's weight (kg): ")

    dog_name = input("Dog's name: ")
    if dog_name == "":
        dog_name = "sweety"

    feeding_hours = input("Feeding hours: ")

    feeding_hours_list = time_feeding(feeding_hours)
    n = len(feeding_hours_list)

    food_amount = get_food_amount(dog_type, dog_weight)

    print(f"\n\x1B[3mAt the automatic dispenser, {dog_name} presses the button and would like to eat...\x1B[0m\n")

    dog_is_hungry(food_amount, feeding_hours_list, dog_name, n)


def pet_type(animal_type):
    # check if the input pet is "dog"
    if not re.search(r"^dog$", animal_type):
        sys.exit("Sorry, only food for dogs")


def time_feeding(feeding_hours):
    feeding_hours_list = []
    # split the input feeding hours into the different hours (they are still str)
    hours = feeding_hours.split(", ")

    # check each str input (with regex); transform each into time format; append each split to the list
    for hour in hours:
        if re.findall(r"^([2][0-3]|[1|0][0-9]):([0-5][0-9])$", hour): # 24h format
            hour = datetime.strptime(hour, '%H:%M').time()
            feeding_hours_list.append(hour)

        elif re.findall(r"^([1][0-2]|([0])[0-9]):([0-5][0-9])(\s(AM|PM))$", hour): # 12h format AM|PM

            if hour.split(" ")[1] == "AM":
                if hour.split(" ")[0].split(":")[0] == "12":
                    hour_hh = hour.split(" ")[0].split(":")[0]
                    hour_hh = "00"
                    hour = hour_hh + ":" + hour.split(" ")[0].split(":")[1]
                    hour = datetime.strptime(hour, '%H:%M').time()
                    feeding_hours_list.append(hour)
                else:
                    hour = hour.split(" ")[0]
                    hour = datetime.strptime(hour, '%H:%M').time()
                    feeding_hours_list.append(hour)

            elif hour.split(" ")[1] == "PM":
                if int(hour.split(" ")[0].split(":")[0]) < 12:
                    hour_hh = int(hour.split(" ")[0].split(":")[0]) + 12
                    hour = str(hour_hh) + ":" + hour.split(" ")[0].split(":")[1]
                    hour = datetime.strptime(hour, '%H:%M').time()
                    feeding_hours_list.append(hour)
                else:
                    hour = hour.split(" ")[0]
                    hour = datetime.strptime(hour, '%H:%M').time()
                    feeding_hours_list.append(hour)

        else:
            sys.exit("Please, insert a correct time format")

    return feeding_hours_list # return at the end/out of the for loop, otherwise after each iteration the code will stop and exit


def dog_weight_modulo(dog_weight):
    # round the input dog weight to the nearest multiple of 5
    dog_weight_mod = int(dog_weight % 5)
    if dog_weight_mod == 3 or dog_weight_mod == 4:
        dog_weight = dog_weight + (5 - dog_weight_mod)
    elif dog_weight_mod == 1 or dog_weight_mod == 2:
        dog_weight = dog_weight - dog_weight_mod

    return dog_weight


def get_food_amount(dog_type, dog_weight):

    if dog_type == "" and dog_weight == "":
        try:
            food_amount = int(input("Food amount: "))
        except ValueError:
            sys.exit("Please, insert any food amount.")

    elif dog_type != "" and dog_weight == "":
        for breed in breeds:
            if breed["breed"] != dog_type:
                continue
            if breed["breed"] == dog_type:
                food_amount = breed["food"]
                break
        else:
            try:
                food_amount = int(input("Food amount: "))
            except ValueError:
                sys.exit("Please, insert any food amount.")


    elif dog_type == "" and dog_weight != "":
        dog_weight = dog_weight_modulo(int(dog_weight))
        for weight in weights:
            if weight["weight"] != dog_weight:
                continue
            if weight["weight"] == dog_weight:
                food_amount = weight["food"]
                break
        else:
            try:
                food_amount = int(input("Food amount: "))
            except ValueError:
                sys.exit("Please, insert any food amount.")



    elif dog_type != "" and dog_weight != "":
        for breed in breeds:
            if breed["breed"] != dog_type:
                continue
            if breed["breed"] == dog_type:
                food_amount = breed["food"]
                break
        else:
            for weight in weights:
                dog_weight = dog_weight_modulo(int(dog_weight))
                if weight["weight"] != dog_weight:
                    continue
                if weight["weight"] == dog_weight:
                    food_amount = weight["food"]
                    break
            else:
                try:
                    food_amount = int(input("Food amount: "))
                except ValueError:
                    sys.exit("Please, insert any food amount.")

    return food_amount


def dog_is_hungry(food_amount, feeding_hours_list, dog_name, n):
    # get the current time
    berlin_tz = pytz.timezone("Europe/Berlin")
    now = datetime.now(berlin_tz)
    current_time = now.strftime("%H:%M")
    current_time = datetime.strptime(current_time, '%H:%M').time()

    # check if the current time corresponds to the settled times, only then print out the amoung of food
    if current_time in feeding_hours_list:
        if n == 0:
            print(f"Don't let {dog_name} starve, choose at least one feeding time!")
        elif n >= 1:
            food_amount = int(food_amount / n)
            print(f"It's time to eat! Here's your food, {dog_name}!🐶\n{food_amount} grams")
    # otherwise exit and say that it's not the right hour
    else:
        print(f"Sorry {dog_name}, it's not the right time to eat.")


if __name__ == "__main__":
    main()
