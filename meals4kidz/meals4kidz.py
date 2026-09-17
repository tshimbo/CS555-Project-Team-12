import re
import unittest
#Terry Shim Contribution
#Story Name:  View measurements
#Task 1: Get measurements of recipe of a specific meal
#Task 2: Print measurements of recipe
#Task 3: Recipe meal cannot be a number

#Sprint 2 Tasks
#Task 4: Must be at least one ingredient per recipe
#Task 5: Recipe must be valid string for ingredient (not a number)
#Task 6: Must have at least one recipe

#Sprint 3 Tasks
#Task 1: ask user to choose specific ingredients for likes
#Task 2: make sure ingredient is valid 
#Task 3: append to list of wanted ingredients

#Sprint 4 Tasks
#Task 1: make sure ingredient is valid (not a number)
#Task 2: find recipes that match list
#Task 3: add more ingredients
#-------------------------------------------------------------------------------

#Example dictionaries for testing purposes

recipesValid = {
        'Rice paper wraps': '1 carrot, 1 avocado, 1/2 cucumber, 8 mint leaves, 50 grams rice vermicelli noodles',
        'Spinach savoury muffins': '200 g fresh spinach, 100g cheddar, 1 tbsp dried thyme, 2 eggs',
        'Omelette': '1 knob of butter, 1 tomato deseeded and diced, 1 tsp dried oregano',
    }

testRecipe = {
        'Rice paper wraps': '1 carrot'
}

recipesInvalidEmptyCase = {
}


recipesInvalidNoIngredients= {
    'Rice paper wraps'
}

recipesInvalidIngredient = {
       'Rice paper wraps': 123
}


ingredientList = ['avocado', 'eggs', 'fish', 'tomato',
                   'peanuts', 'rice', 'spinach', 'broccoli', 'sugar', 'water', 'oil', 'salt', 'fat', 'pork', 'butter', 'apple', 'orange', 
                   'bananas', 'vanilla', 'beef','coconuts', 'thyme'] 

preferencesList = [] #list of preferences to append to


#----------------------------------------------------------------------------------------------------


def checkValidMeal(meal): #checking that a meal cannot be a number
    if meal.isnumeric():
        return False
    else:
        return True
def checkValidRecipe(recipes): #checking that a recipe is valid
    if len(recipes.values()) < 1:
        raise ValueError('Recipe must have at least one ingredient')
    if len(recipes.keys()) < 1:
         raise KeyError('No recipes found')
    for ingredients in recipes.values():
        if ingredients[0].isdigit() :
            return True
        else:
            return False
    for recipe in recipes.keys():
        if isinstance(recipe[0], str):
            return True
        else:
            return False 
        
    return True
        

def measurementList(recipes, meal): #parse through a dictionary of recipes in order to find the measurements of the ingredients
    try:
        # Iterating over values
        assert checkValidMeal(meal) == True   #error checking
        assert checkValidRecipe(recipes) == True 
        print('Measurements of: ' + str(meal) + '\n') #specify which meal you are taking from
        for meal, ingredient in recipes.items():   #iterate through the recipes to find the correct one 
           
            
            return print(ingredient)     #print only the measurement list
    except:
        raise Exception("Meal cannot be a number!")   #error if the meal is a number
        


#-------------------Terry Shim Sprint 3---------------------------------------------------

# ask user if child has favorite ingredients
def hasFavorite():
    while True:
        try:
            x = str(input("Does your child have favorite ingredients? (y/n): "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'y'):
                print('Here are some ingredients your child may like: ')
                print(ingredientList)
                have = True
                break
            elif (x == 'n'):
                have = False
                break
            else:
                print('Please enter y for yes or n for no.')
                continue
    return have

# ask user to input ingredients preferences
def getPreference():
    while True:
        try:
            ingredients = str(input("Enter your child's favorite ingredient: "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            break
    return ingredients


# check if ingredient is already added
def validIngredient(ingredient):
    valid = True
    if (ingredient in preferencesList):
        print("You've already added this ingredient")
        valid = False
    return valid



# ask user if child has another favorite ingredient
def moreIngredient():
    while True:
        try:
            x = str(input("Does your child have another favorite ingredient? (y/n): "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'y'):
                another = True
                break
            elif (x == 'n'):
                another = False
                break
            else:
                print('Please enter y for yes or n for no.')
                continue
    return another


# get list of child's favorite ingredients 
def preferences():
    if not hasFavorite():
        return
    preference = getPreference()
    while not validIngredient(preference):
        preference = getPreference()
    if validIngredient(preference):
        preferencesList.append(preference)
    while moreIngredient():
        preference = getPreference()
        while not validIngredient(preference):
            preference = getPreference()
        if validIngredient(preference):
            preferencesList.append(preference)
    return print("Here is a list of preferred ingredients for your child: " + str(preferencesList))

# find recipe with those matching preferences
def recipesMatchingPreference(preferencesList):
    res = None
    values = []
    items = recipesValid.items()
    for item in items:
       values.append(item[1])
        
    # print("values : ", str(values))

   
    for sub in values:
        if sub in values:
            res = sub
            break
    return print("Here is a recipe that matches favorite ingredients : " + str(res))

#------------------------------------------------------------------------------------------


#############################################################
# Ryan Lee Contribution
# Story Name: Allergies
#
# Sprint #1:
# Task 1: Ask user if child has allergies
# Task 2: Ask user to input child's allergy
# Task 3: Check if child's allergy is a valid
#
# Sprint #2:
# Task 4: Check if child's allergy was already added
# Task 5: Ask user if child has another allergy
# Task 6: Get list of child's allergies
#
# Sprint #3:
# Task 1: Ask user to input medical information
# Task 2: Get height
# Task 3: Get weight
#
# Sprint #4:
# Task 4: Ask user if they would like to use metric or imperial units
# Task 5: Set range for height
# Task 6: Set range for weight
##############################################################
import unittest

commonAllergies = ['dairy', 'eggs', 'fish', 'shellfish',
                   'tree nuts', 'peanuts', 'wheat', 'soy']
allergyList = []


# ask user if child has allergies
def haveAllergy():
    while True:
        try:
            x = str(input("Does your child have allergies? (y/n): "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'y'):
                print('Here are some allergies your child may have: ')
                print(commonAllergies)
                have = True
                break
            elif (x == 'n'):
                have = False
                break
            else:
                print('Please enter y for yes or n for no.')
                continue
    return have


# ask user to input child's allergy
def getAllergy():
    while True:
        try:
            allergy = str(input("Enter your child's allergy: "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            break
    return allergy


# check if allergy is valid or is already added
def validAllergy(allergy):
    valid = True
    if (allergy not in commonAllergies):
        print("This is not a valid allergy")
        valid = False
    if (allergy in allergyList):
        print("You've already added this allergy")
        valid = False
    return valid


# ask user if child has another allergy
def anotherAllergy():
    while True:
        try:
            x = str(input("Does your child have another allergy? (y/n): "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'y'):
                another = True
                break
            elif (x == 'n'):
                another = False
                break
            else:
                print('Please enter y for yes or n for no.')
                continue
    return another


# get list of child's allergies (our main function)
def allergies():
    if not haveAllergy():
        return
    allergy = getAllergy()
    while not validAllergy(allergy):
        allergy = getAllergy()
    if validAllergy(allergy):
        allergyList.append(allergy)
    while anotherAllergy():
        allergy = getAllergy()
        while not validAllergy(allergy):
            allergy = getAllergy()
        if validAllergy(allergy):
            allergyList.append(allergy)
    return allergyList


################### Ryan Lee Sprint 3/4 ########################

# ask user to input medical information
def getMedInfo():
    metric = getUnit()
    if metric:
        print("Please input your child's height (cm) and weight (kg) below:")
        height = getHeight()
        while not validHeight(height):
            height = getHeight()
        weight = getWeight()
        while not validWeight(weight):
            weight = getWeight()
        print("Height: " + str(height) + " cm")
        print("Weight: " + str(weight) + " kg")
    else:
        print("Please input your child's height (in) and weight (lb) below:")
        height = getHeight()
        cm = inToCM(height)
        while not validHeight(cm):
            height = getHeight()
            cm = inToCM(height)
        weight = getWeight()
        kg = lbToKG(weight)
        while not validWeight(kg):
            weight = getWeight()
            kg = lbToKG(weight)
        print("Height: " + str(height) + " in")
        print("Weight: " + str(weight) + " lb")


# get height
def getHeight():
    while True:
        try:
            height = float(
                (input("Enter your child's height: ")))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    return height


# get weight
def getWeight():
    while True:
        try:
            weight = float(
                (input("Enter your child's weight: ")))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    return weight


# get unit
def getUnit():
    while True:
        try:
            x = str(
                (input("Metric or imperial units ('m' for metric, 'i' for imperial): ")))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'm'):
                metric = True
                break
            elif (x == "i"):
                metric = False
                break
            else:
                print('Please enter m for metric or i for imperial.')
                continue
    return metric


# convert inches to centimeters
def inToCM(inch):
    return inch * 2.54


# convert pounds to kilograms
def lbToKG(lb):
    return lb / 2.205


# set range for height
def validHeight(cm):
    valid = True
    if (cm < 45 or cm > 215):
        print("Height out of range")
        valid = False
    return valid


# set range for weight
def validWeight(kg):
    valid = True
    if (kg < 2 or kg > 150):
        print("Weight out of range")
        valid = False
    return valid

#_____________________________________________________________

# Maksym Perozhak Contribution

# Sprint 1
# Story Name: Choose Age
# Sprint 1 Task 1: Identify the age of the user
# Sprint 1 Task 2: Identify if age of user old enough for app authorization
# Sprint 1 Task 3: Identify if age of user is valid

#_____________________________________________________________

from datetime import datetime, date
 
def checkValidUserAge(birthdate):
    today = date.today()
    #birthdate = datetime.fromisoformat(input("Enter Your Birthdate in YYYY-MM-DD Format: "))
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 18:
        return ("User Age Verified!")
    elif age < 18 and age > 0:
        return ("Sorry, you are not eligable")
    elif age <= 0:
        return ("Please Enter A Valid Date")
    else:
        return ("Please Enter Your Birthdate in YYYY-MM-DD Format")

#_____________________________________________________________

# Sprint 2
# Story Name: Choose Age
# Sprint 2 Task 1: Identify the age of the child
# Sprint 2 Task 2: Identify what age range category diet the child belongs to
# Sprint 2 Task 3: Identify if age of the child is valid

#_____________________________________________________________

def childAge(birthdate):
    dietRange = ""
    today = date.today()
    #birthdate = datetime.fromisoformat(input("Enter Your Birthdate in YYYY-MM-DD Format: "))
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age < 1:
        dietRange = "baby"
        return("Your child is less than a year old \n Reccomended Diet For: Baby")
    elif age < 4 and age >= 1:
        dietRange = "toddler"
        return("Your child is " + str(age) + " years old \n Reccomended Diet For: Toddler")
    elif age < 12 and age >= 4:
        dietRange = "young"
        return ("Your child is " + str(age) + " years old \n Reccomended Diet For: Young Child")
    elif age < 18 and age >= 12:
        dietRange = "teen"
        return("Your child is " + str(age) + " years old \n Reccomended Diet For: Teen")
    elif age >= 18:
        dietRange = "adult"
        return ("Your child is 18 years old or older and should be considered for adult diets")
    else:
        return ("Please Enter Your Birthdate in YYYY-MM-DD Format")

#_____________________________________________________________

# Sprint 3
# Story Name: Track Growth
# Sprint 3 Task 1: Input the child's age
# Sprint 3 Task 2: Input the child's weight for each age in a dictionary
# Sprint 3 Task 3: Save the data to be opened up later to see the childs weight history

#_____________________________________________________________


import json
import os

# Data files live next to this script so the app works from any directory.
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
WEIGHTS_FILE = os.path.join(DATA_DIR, 'weightsFile.json')
HEIGHTS_FILE = os.path.join(DATA_DIR, 'heightsFile.json')


def loadHistory(path):
    """Return saved history, or an empty dict if the file is missing or empty."""
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return {}
    with open(path) as f:
        return json.load(f)

weights = loadHistory(WEIGHTS_FILE)

def addWeight(age, weight):
    weights[age] = weight
    return weights

def clearWeight():
    weights.clear()
    open(WEIGHTS_FILE, 'w').close()

def displayWeightHistory():
    print("{:<10} {:<10}".format('Age', 'Weight'))
    for key, value in weights.items():
        weight = value
        print("{:<10} {:<10}".format(key, weight))

with open(WEIGHTS_FILE, 'w') as f:
    json.dump(weights, f)

#_____________________________________________________________

# Sprint 4
# Story Name: Track Growth (height)
# Sprint 4 Task 1: Input the child's age
# Sprint 4 Task 2: Input the child's height for each age in a dictionary
# Sprint 4 Task 3: Save the data to be opened up later to see the childs height history

#_____________________________________________________________

heights = loadHistory(HEIGHTS_FILE)

def addHeight(age, height):
    heights[age] = height
    return heights

def clearHeight():
    heights.clear()
    open(HEIGHTS_FILE, 'w').close()

def displayHeightHistory():
    print("{:<10} {:<10}".format('Age', 'Height'))
    for key, value in heights.items():
        height = value
        print("{:<10} {:<10}".format(key, height))

with open(HEIGHTS_FILE, 'w') as f:
    json.dump(heights, f)

#--------------------------------------
#Testing functions
class Test(unittest.TestCase):
    def test_checkValidUserAge(self):
        print("\n")
        print(checkValidUserAge(date(2000, 10, 10)))
        print(checkValidUserAge(date(2010, 1, 1)))
        print(checkValidUserAge(date(2030, 1, 1)))
        print("\n")

    def test_checkWeightHistory(self):
        clearWeight()
        print(addWeight(6, 80))
        print(addWeight(7, 90))
        print(addWeight(8, 100))
        displayWeightHistory()

    def test_checkHeightHistory(self):
        clearHeight()
        print(addHeight(6, 48))
        print(addHeight(7, 60))
        print(addHeight(8, 72))
        displayHeightHistory()
    
    def test_childAge(self):
        print("\n")
        print(childAge(date(2002, 1, 1)))
        print(childAge(date(2008, 1, 1)))
        print(childAge(date(2014, 1, 1)))
        print(childAge(date(2019, 1, 1)))
        print(childAge(date(2022, 1, 1)))
        print("\n")

    def test_checkValidMeal(self):
        self.assertTrue(checkValidMeal('omelette'), 'omelette')
        self.assertFalse(checkValidMeal('123'), '123')
    
    def test_checkValidRecipe(self):
        self.assertTrue(checkValidRecipe(recipesValid))
        with self.assertRaises(ValueError):
            checkValidRecipe(recipesInvalidEmptyCase)
        with self.assertRaises(AttributeError):   
            checkValidRecipe(recipesInvalidNoIngredients)
        with self.assertRaises(TypeError):
            checkValidRecipe(recipesInvalidIngredient)
        
    def test_measurementList(self):
        self.assertFalse(measurementList(recipesValid,'Omelette'), "432")

    def test_validAllergy(self):
        self.assertTrue(validAllergy("fish"), "fish")
        self.assertTrue(validAllergy("soy"), "soy")
        self.assertFalse(validAllergy("555"), "fish")

    def test_validIngredient(self):
        print("\n")
        self.assertTrue(validIngredient("potato"), "potato")
        self.assertTrue(validIngredient("eggs"), "eggs")
        self.assertTrue(validIngredient("spinach"), "spinach")
        self.assertTrue(validIngredient("rice"), "rice")
        self.assertTrue(validIngredient("tomato"), "tomato")
        print("\n")


if __name__ == '__main__':
    unittest.main()

#_______________________________________________________________________________________________

import unittest
#Sprint 1
#Pratik Kadam contribution
#Story name: Find recipes
#Task 1 : Define the dishes
#Task 2: Define the ingredients of the respective dishes
#Task 3: Ask the user to choose their desired dish

dishes=['chicken','oatmeal','bagel','omlette','breadtoast']
chicken=['salt','pepper','chicken breast']
oatmeal=['oats','milk','berries','nuts','fruits']
bagel=['bagel','creamcheese']
omlette=['eggs','salt','tomato','oregano']
breadtoast=['bread','butter']

def validRecipes():
    while True:
        try:
            print(f"{dishes}")
            x= str(input("Select the dish of your choice: ")) #taking input from user for the choice of dish
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if(x=='chicken'):
                print(f"{chicken}")
                break
            elif(x=='oatmeal'):
                print(f"{oatmeal}")
                break
            elif(x=='bagel'):
                print(f"{bagel}")
                break
            elif(x=='omlette'):
                print(f"{omlette}")
                break
            elif(x=='breadtoast'):
                print(f"{breadtoast}")
                break
            else:
                print('Please enter valid dish')
                continue
    return validRecipes

validRecipes()

class Test(unittest.TestCase):

    def test_ValidRecipes(self):
        self.assertTrue(validRecipes('chicken'), 'chicken')
        self.assertTrue(validRecipes('oatmeal'), 'oatmeal')
        self.assertTrue(validRecipes('bagel'), 'bagel')
        self.assertTrue(validRecipes('omlette'), 'omlette')
        self.assertTrue(validRecipes('breadtoast'), 'breadtoast')
        self.assertFalse(validRecipes('123'), '123')

if __name__=='__main__':
    unittest.main()

#____________________________________________________________________________________________________________________________
#Sprint 2
#Pratik Kadam contribution
#Story name : Encryption
#Task 1: Ask the user to create username and password.
#Task 2: Ask the user to enter the created username and password for login.
#Task 3: To check if the entered credentials match and display the recipes.

import unittest

def register():
    Username=str(input("Create username: "))
    Password=str(input("Create password: "))
    Password1=str(input("Confirm password: "))

    if Password != Password1:
        print("Password donot match, please retry")
        register()
    else:
        if len(Password)<=10 or len(Password)>=16:
            print("Password not in range, please restart")
            register()
        elif len(Username)<=5 or len(Username)>=11:
            print("Username not in range, please restart")
            register() 
        else:
            print("Success!")
            creddict={"Username":Username, "Password":Password}
            
            def login():
                Username1=str(input("Enter username:"))
                Password2=str(input("Enter password:"))
                if Username1!=Username or Password2!=Password:
                    print("Wrong credentials, retry")
                    login()
                elif Username1==Username and Password2==Password:
                    print("Logging in!")
                    from recipes import validRecipes
            login()

register()

class Test(unittest.TestCase):

    def test_Register(self):
        self.assertEqual(register(''), 'Empty')
        self.assertEqual(register('Happyhalloween2022'), 'Out of range')

if __name__=='__main__':
    print("Running unit tests")
    unittest.main() 

#______________________________________________________________________________________________________________
#Sprint 3:
#PratikKadam contribution
#Storyname: Encryption
#Task 1: Asked the user to create username and password
#Task 2: Stored the credentials in a text file


def registr():

    db=open("database.txt","r")
    Username=input("Create username:")
    Password=input("Create password:")
    Password1=input("Confirm password")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))
    print(data)

    if Password != Password1:
        print("Passwords don't match, restart")
        registr()
    else:
        if len(Password)<=6:
            print("Password too short, restart")
            registr()

        else:
            db=open("databas.txt","a")
            db.write(Username+","+Password+"\n")
            print("Success")

registr()

    
def access():
    pass

#-----------------------------------------------------------------------------------------------------------------------------------
#Sprint 4:
#Pratik Kadam contribution:
#Storyname: Encryption
#Task 1: Hashing of stored from user database
#Task 2: Checking if the plain text password matches with hashed password
#Task 3: Increasing the work factor to slow down hashing and vice versa

import bcrypt
password=b"hellounitedstatesofamerica"
hashed=bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
"""b'$2b$12$XqDv65ssdxPCy8PBKoOYUuza/oblze2.kn7i/e7qDmBC3aWhMVL.q"""
#---------------------------------------
import bcrypt
password=b"hellounitedstatesofamerica"
"""hashed=bcrypt.hashpw(password, bcrypt.gensalt())"""
#print(hashed)
"""b'$2b$12$XqDv65ssdxPCy8PBKoOYUuza/oblze2.kn7i/e7qDmBC3aWhMVL.q"""
if bcrypt.checkpw(password,hashed):
    print("Password matches")
else:
    print("Password doesn't match")
#---------------------------------------
import bcrypt
password=b"hellounitedstatesofamerica"
import time 
start=time.time()
hashed=bcrypt.hashpw(password, bcrypt.gensalt())
end=time.time()
f= end-start
print(f)
#--------------------------------------------
import bcrypt
password=b"hellounitedstatesofamerica"
import time 
start=time.time()
hashed=bcrypt.hashpw(password, bcrypt.gensalt(rounds=20))
end=time.time()
f= end-start
print(f)
#-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#Michael Moreno
#Story Name: Nutrition facts

#Task 1: Define the dish
#Task 2: retrieve ingredient list and assign caloric values to ingredients
#Task 3: calculate total calories as sum of ingredients
import unittest

#Sprint 2
#Task 1: display list of recipes instead of asking for input
#Task 2: add more recipes
#Task 3: make sure a valid dish is entered

#This portion requires onetimepass package in python, install using 'pip install onetimepass' in command window to avoid issues when running code
#Sprint 3: 2FA
#Task 1: Instruct user to download microsoft authenticator or authy
#Task 2: Display secret key so user can connect their app to their account
#Task 3: Authenticate and connect their account

#define dish
#retrieve ingredient list and assign caloric values to ingredients
#arbitrary values for ingredients
recipe_list = ['oatmeal', 'parfait', 'acai', 'pancakes', 'waffles', 'omelette']

oatmeal = {
    'oats': 100,
    'milk': 500,
    'sugar': 200,
    'strawberries': 150}

parfait = {
    'yogurt': 300,
    'strawberries': 100,
    'blueberries': 150,
    'granola': 100}

acai = {
    'acai puree': 200,
    'bananas': 150,
    'strawberries': 150,
    'blueberries': 150,
    'granola': 100,
    'kiwi': 100
    }

pancakes = {
    'pancakes': 400,
    'syrup': 150,
    'bananas': 100
    }

waffles = {
    'waffles': 400,
    'syrup': 150,
    'sugar': 200,
    'strawberries': 200
    }

omelette = {
    'eggs': 500,
    'tomatoes': 100,
    'ham': 300,
    'salt': 100,
    'pepper': 100,
    }

#calculate calorie total by adding caloric values of ingredients
def CalcCals():
    print(recipe_list)
    while True:
        try:recipe= str(input("Please choose a recipe from the list: "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if recipe=='oatmeal':
                print(sum(oatmeal.values()), 'Calories')
                break
            elif recipe=='parfait':
                print(sum(parfait.values()), 'Calories')
                break
            elif recipe=='acai':
                print(sum(acai.values()), 'Calories')
                break
            elif recipe=='pancakes':
                print(sum(pancakes.values()), 'Calories')
                break
            elif recipe=='waffles':
                print(sum(waffles.values()), 'Calories')
                break
            elif recipe=='omelette':
                print(sum(omelette.values()), 'Calories')
                break
            else: print('please enter a valid dish.')
            continue

CalcCals()

#Sprint 3
from onetimepass import valid_totp
from secrets import choice


def generate_key():  # Function to return a random string with length 16.
    key = ''
    while len(key) < 16:
        key += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
    return key

def validate_key():
    key = generate_key()
    print('Enter the following secret in your authenticator app: ', key)
    print("""
    Instructions for entering this key in your authenticator app:
    1. Open authenticator app.
    2. Click plus icon to add account.
    3. Click enter key manually.
    4. Enter an account name of your choice and enter the key provided above.
    5. Click Add.
    """)
    while True:
        otp = int(input('Please enter the otp generated by your authenticator app: '))
        authenticated = valid_totp(otp, key)
        if authenticated:
            print('Correct otp, Authenticated!')
            return
        elif not authenticated:
            print('Wrong otp, please try again.')
    return

validate_key()


class Test(unittest.TestCase):

    def test_CalcCals(self):
        self.assertEqual(CalcCals, 950)
        self.assertEqual(CalcCals, 1000)
        self.assertEqual(CalcCals, 0)
       
if __name__ == '__main__':
    unittest.main()

#----------------------------------------------------------------------------------------------------------------------------
#Kevin Liao Contribution
#Story Name: Recipe Preferences
#Sprint 3 Tasks
#Task 1: Allow users to save recipes
#Task 2: Find if the saved recipes contain preferred ingredients
#Task 3: Print recipes which have half of their ingredients as preferred ingredients

import unittest

ingredientList = ['avocado', 'eggs', 'fish', 'tomato',
                   'peanuts', 'rice', 'spinach', 'broccoli']

preferencesList = ["carrot", "avocado", "cucumber", "mint leaves", "spinach", "cheddar"]

recipesValid = {
        'rice paper wraps': '1 carrot, 1 avocado, 1/2 cucumber, 8 mint leaves, 50 grams rice vermicelli noodles',
        'spinach savoury muffins': '200 g fresh spinach, 100g cheddar, 1 tbsp dried thyme, 2 eggs',
        'omelette': '1 knob of butter, 1 tomato deseeded and diced, 1 tsp dried oregano',
    }


# Adds a recipe to recipesValid with its ingredients
def addRecipe():
    while True:
        try:
            newRecipe = str(input("Enter the name of a new recipe: "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if(newRecipe in recipesValid):
                print("This recipe is already added.")
                break
            else:
                if (newRecipe == ""):
                    print("Recipe is unnamed.")
                    break
                recipesValid[newRecipe] = ""
                while True:
                    try:
                        newRecipeIngredient = str(input("Enter an ingredient for this recipe (Type Finished if the recipe is finished): "))
                    except ValueError:
                        print("Please enter a string")
                        continue
                    else:
                        if (newRecipeIngredient in recipesValid[newRecipe]):
                            print("That ingredient is already in the recipe")
                            continue
                        elif (newRecipeIngredient == ""):
                            continue
                        elif (newRecipeIngredient == "Finished"):
                            recipesValid[newRecipe] = recipesValid.get(newRecipe)[:-2]
                            print(newRecipe + ": " + recipesValid[newRecipe])
                            return    
                        else:
                            recipesValid[newRecipe] = recipesValid.get(newRecipe) + newRecipeIngredient + ", "
                            continue

# Finds recipes in recipe dictionary that have 50% or more of the ingredients from the preferred ingredients dictionary               
def searchPreferenceRecipe():
    similar = 0
    for recipes in recipesValid:
        for n in range(0, len(preferencesList)):
            if(preferencesList[n] in recipesValid[recipes]):
                similar += 1
        if(similar >= (recipesValid[recipes].count(',') + 1)/2):
            print(recipes + " has " + str(similar) + " out of " + str(recipesValid[recipes].count(',') + 1) + " ingredients you like.") 
            similar = 0
    return


#----------------------------------------------------------------------------------------------------------------------------
#Sprint 4 Tasks
#Task 1: Get user input for a recipe they like
#Task 2: Get user to input ingredients of that recipe they like
#Task 3: Add those liked ingredients to the ingredients preference list

# Finds recipes in recipe dictionary that is similar to another dictionary (shares 50% of ingredients)
def favIngredientsOfRecipe():
    while True:
        try:
            typeRecipe = str(input("Which recipe do you want to select?: ")).casefold()
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if(typeRecipe not in recipesValid):
                print("This recipe is is not added.")
                break
            else:
                if (typeRecipe == ""):
                    print("Recipe is unnamed.")
                    break
                print(typeRecipe + ": " + recipesValid[typeRecipe])
                while True:
                    try:
                        # typeRecipe = "Rice paper wraps"
                        typeRecipeIngredient = str(input("What ingredients of this recipe do you like? (Type Finished if finished): ")).casefold()
                    except ValueError:
                        print("Please enter a string")
                        continue
                    else:
                        if (typeRecipeIngredient == "finished"):
                            # recipesValid[typeRecipe] = recipesValid.get(typeRecipe)[:-2]
                            # print(typeRecipe + ": " + recipesValid[typeRecipe])
                            print("The current preferences list:")
                            print(preferencesList)
                            return
                        elif (typeRecipeIngredient not in recipesValid[typeRecipe].casefold()):
                            print("That ingredient is not in the recipe")
                            continue
                        elif (typeRecipeIngredient in preferencesList):
                            print("This ingredient is already in the preferences list")
                            continue
                        elif (typeRecipeIngredient == ""):
                            continue  
                        else:
                            preferencesList.append(typeRecipeIngredient)
                            continue
    
# favIngredientsOfRecipe()


