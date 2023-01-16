# CS50-s-Introduction-to-Programmign-with-Python---Final-Project
# The dog is hungry
## Video Demo:  <https://youtu.be/99l4-jTTNik>
## Description
## Summary
<div style="text-align: justify"> The program mimics an automatic dispenser to feed dogs only.

As first filter, if the user types a type of pet that is not dog, the programs exits and ends. Otherwise, if the user inserts "dog" (case insesitevely), the program will proceed. If the time when the dog metaphorically presses the button on the automatic dispenser corresponds to at least on of the settled feeding times, the dog is fed with virtual food, that means displayed amount of grams.

Certain settings can be decided at the beginning of the program, as prompted inputs to the users. These are the dog's breed, the dog's weight, if the previous two are not given then the food amount is asked, then the dog's name, and the hours when the user (owner) would like to feed the dog. Depending on these initial inputs, then the given amount of food varies, for example if the dog's breed is Newfoundland, the dog will receive more food (900 g) than a Yorkshire breed (100 g). Similarly, if the dog's weight is 45 kg, the dog will receive more food (900 g) than a 5 kg dog (100 g). If the user inputs the dog's breed but not the weight, the first will be used as reference to output the food amount, and likewise the other way around. The related breeds-food amount and weight-food amount are saved in two lists of dictionaries. The program will then go through either one of them to find out the right food amount to give. If the user doesn't insert any of the previous inputs, then the program will ask directly how much food amount the user (owner) would like to give.

Finally, independently on the breed or weight, if the dog virtually "presses the button" on the automatic dispenser to eat at a time that doesn't correspond to the settled times, then no food is virtually given. On the other hand, if the time is right then the dog will receive its virtual food in form of displayed grams fo food (for example "700 grams").</div>


## Libraries
<div style="text-align: justify"> In order to run the program I included few libraries. Please, find them listed in the table below with the related use in the program. </div>

| Library name  | Library use |
| ------------- | ------------- |
| re            | Used to check if the input "type of pet" is equal to "dog" and used to check if the input "feeding times" are in the right format (24h or 12h AM\|PM) |
| sys           | Used to exit the program when the input for pet type is not "dog", when the feeding hours are not inserted in the right format |
| datetime      | Used to transform the inserted feeding hours from str to the time format "%H:%M", in order to be able to then compare it with the current time |
| pytz | Used to obtained the current time in the time zone 'Europe/Berlin'  |



## Paramters/inputs as settings of the automatic dispenser
<div style="text-align: justify"> Once the program is run, two lists of dogs' breeds and dogs' weights are printed. These are the key values of two lists of dictionaries. The names and contents of these two lists are shown in the table below. In both lists, the values of the key "food amount" are expressed in grams, and are of type int. The values of the key "breed" in the list breeds are of type str. The values of the key "weight" in the list weights are expressed in kg, and are of type int. The values of the keys can be expanded or corrected if necessary. </div>

| List of dictionary name  | List of dictionaries keys | List of dictionaries values |
| ------------------------ | ---------------------------- | ---------------------------- |
| breeds                   | "breed" | "Golden retriever", "Newfoundland", "Labrador retriever", "Border collie", "Australian sheperd", "Yorkshire", "Bulldog", "Bernese mountain" |
|                    | "food amount" | 700, 900, 700, 500, 600, 100, 300, 900|
| weights                   | "weight" | 45, 40, 35, 30, 25, 20, 15, 10, 5 |
|                    | "food amount" | 900, 800, 700, 600, 500, 400, 300, 200, 100 |

<div style="text-align: justify">Afterwards, the message "Settings of the automatic feeding dispenser:" is displayed to inform the user that certain information should be inserted.

- animal_type

The first information to insert is the type of pet that the user has (str type). If the user types "dog" (case insensitive), the program will go on with the next steps. Otherwise, the program will exit.

- dog_type

The second information is related to the breed of the dog (str type). The user is asked to insert the breed of the dog, among the values of the breeds dictionary. If the breed is unknown or cannot be specified or not in the list of values, this input can be skipped without any error raising. By simply pressing enter, the user can then insert the weight of the dog if known (see next, dog_weight).

- dog_weight

Afterwards, the user is asked to insert the weight of the dog in kg,  that are listed in the weights list of dictionaries (int type). If the breed is unknown or cannot be specified or not in the list of values, this input can be skipped without any error raising. By simply pressing enter, the user can then insert the weight of the dog if known (see next, dog_weight).

- dog_name

The fourth input is related to the dog's name (str type). The user is asked to insert the name of the dog, however if nothing is input no error will raise but "sweety" will be assigned to it.

- feeding_hours

At this point, the user is asked to insert the times (hours) when the dog should be fed. Either one or more times can be inserted, separating each of them with ", ". The two possible formats are 24h or 12h AM|PM. Here some examples:

24h format: hh:mm OR hh:mm, hh:mm OR hh:mm, hh:mm, hh:mm etc

12h format: hh:mm AM|PM OR hh:mm AM|PM, hh:mm AM|PM OR hh:mm AM|PM, hh:mm AM|PM, hh:mm AM|PM etc

The type is str, and it will be transformed in datetime later in the program.

Note: to see the virtual automatic dispenser actually feeding the virtual dog, I suggest to try to type at least in one time the current hour (e.g. if it's 10:24 AM, type 10:24 AM when "Feeding hours: " appears).

- feeding_hours_list

This is the list of times (hours) saved as datetime "%H:%M". This is the output of the function time_feeding (see later).

- n

This represents the length of the mentioned list of datetime times. </div>

## Functions

<div style="text-align: justify">Apart from the main function, five other functions were created for the good working of the program. The names, passed parameters and outputs are listed in the table below. </div>

| Function name  | Function parameters | Function output |  |
| ------------------------ | ---------------------------- | ---------------------------- | -------------------------- |
| pet_type                   | animal_type.lower() | - |  |
| time_feeding               | feeding_hours | feeding_hours_list |  |
| get_food_amount            | dog_type, dog_weight | food_amount |  |
| dog_weight_modulo          | dog_weight | dog_weight |  |
| dog_is_hungry              | food_amount, feeding_hours_list, dog_name, n | - |  |


- pet_type

<div style="text-align: justify">At the very beginning of the program (in main), this checks if the input animal_type is equal to "dog" (case insensitive). If it corresponds, the program continues (prompted inputs and next functions). Otherwise, the program ends, specifying "Sorry, only food for dogs". </div>


- time_feeding


<div style="text-align: justify"> After inserting the wanted inputs (see before, Settings), this function proceeds to transform the str times into datetime format. At first the input value/s are splitted and saved in a new list. Afterwards, the functions checks if the inserted value/s correspond/s to the wanted format (see feeding_hours description), by using regex. For the 24h format case, if the inserted value is correct, the function then proceeds to transform the str value into a datetime value, using the library datetime/datetime, with datetime.strptime(str, '%H:%M').time(). For the 12h format case, if the inserted value is correct, the function then proceeds to transform the time into a 24h format and into a datetime format. It deletes the "AM" or "PM"; if "PM" is inserted and if the hour is lower than 12, it adds 12 to it, otherwise it remains as it is. If "AM" is inserted and if the hour is equal 12, the hour is transformed to 00, otherwise it reamins as it is. In both cases, the str is finally transformed into a datetime format. In both 24h and 12h cases, the new datetime elements are appended to an list previously created (feeding_hours), and returned. </div>

- get_food_amount

<div style="text-align: justify"> The program proceeds to obtain the amount of food depending on either the inserted breed or the inserted weight, or if none of the previous are given, to directly ask for an amount ot the owner. It takes into account four cases: 1. if no breed nor weight are insesrted, 2. if breed is inserted but no weight, 3. if no breed is inserted but weight is, 4. if both breed and weight are inserted. In the first case, the owner is asked to directly insert a food amount as input. In the second case, the program goes through the list of dictionaries "breeds" to look for the inserted value. If it's found, then the amount of food related to that breed is assigned to the "food_amount" variable. Otherwise if the inserted breed is not in the list or is wrongly typed, the owner is asked to directly insert a food amount as input. In the third case, the program goes through the list of dictionaries "weights" to look for the inserted value. If it's found, then the amount of food related to that weight is assigned to the "food_amount" variable. Otherwise if the inserted weight is not in the list or is wrongly typed, the owner is asked to directly insert a food amount as input. In the fourth case, the program goes through the list of dictionaries "breeds" to look for the inserted value. If it's found, then the amount of food related to that breed is assigned to the "food_amount" variable. Otherwise if the inserted breed is not in the list or is wrongly typed, the program goes through the list of dictionaries "weights" to look for the inserted value. If it's found, then the amount of food related to that weight is assigned to the "food_amount" variable. Otherwise if the inserted weight is not in the list or is wrongly typed, the owner is asked to directly insert a food amount as input. In the cases where the inserted dog_weight should be used, another function is called (dog_weight_modulo), to round up or down the value to the nearest multiple of 5. </div>

- dog_weight_modulo

This function is called from the get_food_amount function, in order to round up or down the inserted dog_weight value to the nearest multiple of 5. In this case, modulo of dog_weight, subtractions and additions are used. For example if the inserted dog_weight is 21 or 22, it is rounded to 20; if it is 23 or 34 it rounded to 25.

- dog_is_hungry

Once all the settings are fixed and ready, the program then proceeds to the dog feeding part. First, the function gets the current time, in teh Europe/Berlin timezone, as 24h format using the pytz library. Afterwards, if at least one of the previously selected feeding time/hours correspond to the current time, then the virtual dispenser will give the right amount of food (obtained from the get_food_amount function), as follows:

> It's time to eat! Here's your food, {dog_name}!🐶

> {food_amount} grams

where {dog_name} is substituted with either the inserted name fo the dog, or if nothing inserted with "sweety"; and where {food_amount} is substituted with the right food amount as int from the get_food_amount function.

In this case, if the number of selected times is more or equal to 1, then the amount of food is divided into this number (e.g. if the feeding hours are 08:30, 12:30, 16:30, and the food amount is 900 grams, then the amount of food that is given at the current time is 900 / 3 = 300 grams). If the number of times is 1, the whole food amount will eb given and if the number fo times is 0, then an encouraging message of not to starve the dog is dispalyed. Otherwise, if the previously selected feeding times do not correspond to the current time, then the followign message is displayed:
> Sorry {dog_name}, it's not the right time to eat.
