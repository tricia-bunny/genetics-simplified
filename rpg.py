import random
from collections import namedtuple
personAttributes = namedtuple('personAttributes',
                              'firstname, lastname, strength, intelligence, agility, charisma, instinct, gender, bodyColor, finColor, eyeColor, momGenetics, dadGenetics')
title = "Fishland: A Role-Play Game"

fishArray = {}
missionArray = {}
items = {}
"""
colors:
0-undecided
1-crimson
2-carmine
3-vermillion
4-bright orange
5-pale orange
6-orange-yellow
7-sunrise yellow
8-lemon yellow
9-yellow-green
10-lime green
11-mint green
12-grass green
13-forest green
14-dark teal
15-teal
16-sea blue
17-ice blue
18-sky blue
19-twilight
20-parma
21-imperial violet
22-jet black
23-dark brown
24-dark gray
25-light gray
26-soft gray-white
27-white
28-baby pink
29-soft pink
30-bubblegum-pink
31-neon pink
32-coral pink

onePerson =  personAttributes()
onePerson.gender
"""
colors = ['crimson', 'carmine', 'vermillion', 'bright orange', 'pale orange', 'orange-yellow', 'sunrise yellow',
          'lemon yellow', 'yellow-green', 'lime green', 'mint green', 'grass green', 'forest green', 'dark teal',
          'teal', 'sea blue', 'ice blue', 'sky blue', 'twilight', 'parma', 'imperial violet', 'jet black', 'dark brown',
          'dark gray', 'light gray', 'soft gray-white', 'white', 'baby pink', 'soft pink', 'bubblegum-pink',
          'neon pink', 'coral pink']

fishMap = [
    '             1         2         3         4                ',
    '    12345678901234567890123456789012345678901234567         ',
    ' 1        @@@@                                              ',
    ' 2      @@@@@@                                              ',
    ' 3      @@@@@@@@@                                           ',
    ' 4       @@@@@@@@@                                          ',
    ' 5      bbbb@@@ffffff=======llll                            ',
    ' 6    bbbbbbbfffffff========lllllll                         ',
    ' 7    bbbbbbfffffff==========llllllll                       ',
    ' 8    bbbb######oooo========ssssllllll                      ',
    ' 9      b#######oooo%%%%%%%^^^sssss::::                     ',
    '10     kk#######ooooo%%%%%%^^^sssss::::::::                 ',
    '11     kkkkkkkoooooooo%%%%%%^^sssss:::::::::::              ',
    '12       kkkkk***oo**%%%%%%%s^^sssq:::::::::eeeee           ',
    '13         kkkk*******%%%%tttt^^sqqqqqq:::::::eeeeee        ',
    '14          kkk**********%%tttt^^qqqqqqq:::::eeeeee&&       ',
    '15            k***********tttttt^^^qqqqjjjjjeeeee&&&&       ',
    '16             ******tttttttttttt^^$$$jjjjjjjjjj&&&         ',
    '17                 *tttttttttttt^^^^$$$$jjjjjjjj&&          ',
    '18                      ttttttttt^^^$$$$$$jjjjj&&           ',
    '19                         tttttt^^^$$$$$$$jjjj&&           ',
    '20                              $$^^$$$$$$jjj&&&&           ',
    '21                                $^$$$$$jjj&&&&&&          ',
    '22                                 $^$$$$$jj&&&&&           ',
    '                                                            '
]

# These are our fish
# ZERO GENERATION
xenon = personAttributes('Xenon', 'the Fish', 10, 6, 9, 14, 3, 'Female', 'vermillion', 'carmine', 'dark teal', None,
                         None)
pygame = personAttributes('Pygame', 'the Fish', 19, 4, 19, 19, 3, 'Male', 'dark gray', 'vermillion', 'lemon yellow',
                          None, None)
radone = personAttributes("Radone", "the Fish", 2, 3, 16, 8, 19, 'Female', 0, 0, 0, None, None)
sys_fish = personAttributes("Sys", "the Fish", 1.5, 19, 16, 19, 10, 'Male', 0, 0, 0, None, None)
cashmere = personAttributes("Cashmere", 'the Fish', 2, 10, 3, 16, 19, 'Female', 0, 0, 0, None, None)
ellipse = personAttributes("Ellipse", 'the Fish', 19, 2.0, 9, 0.5, 2.0, 'Male', 0, 0, 0, None, None)
perimeter = personAttributes("Perimeter", "the Fish", 16, 2.0, 2, 1.5, 3, 'Female', 0, 0, 0, None, None)
area = personAttributes("Area", "the Fish", 13, 12, 15, 29, 8, 'Male', 0, 0, 0, None, None)
angle = personAttributes("Angle", 'the Fish', 13, 2, 3, 2.0, 2.0, 'Female', 0, 0, 0, None, None)
degree = personAttributes("Degree", "the Fish", 19, 12, 15, 0.5, 10, "Male", 0, 0, 0, None, None)
# FIRST GENERATION
fidget = personAttributes("Fidget", "the Fish", 19, 6, 19, 19, 3, "Female", 'sunrise yellow', 'vermillion', 'dark teal',
                          xenon, pygame)
theBoys_Sikell = personAttributes("'The Boys'", "the Fish", 3, 19, 16, 19, 19, "Male", 0, 0, 0, radone, sys_fish)
bob = personAttributes("Bob", "the Fish", 19, 20, 9, 8, 38, "Male", 0, 0, 0, cashmere, ellipse)
scalene = personAttributes("Scalene", "the Fish", 16, 24, 15, 29, 8, "Male", 0, 0, 0, perimeter, area)
isosceles = personAttributes("Isosceles", "Polygon", 19, 12, 15, 1, 20, "Female", 0, 0, 0, angle, degree)
# SECOND GENERATION
kale = personAttributes("Kale", "the Fish", 19, 8, 9, 19, 19, "Female", 'grass green', 'mint green', 'twilight', fidget,
                        bob)
triangle = personAttributes("Triangle", "Polygon", 19, 12, 15, 1, 10, "Male", 0, 0, 0, isosceles, scalene)
radius = personAttributes("Radius", "Polygon", 19, 12, 15, 10, 10, "Male", 0, 0, 0, isosceles, scalene)
# THIRD GENERATION
fish = personAttributes("Fish", "the Fish", 29, 38, 16, 19, 19, "Male", 0, 0, 0, kale, theBoys_Sikell)
pi = personAttributes("π", "the Fish", 29, 38, 16, 19, 10, "Female", 0, 0, 0, kale, theBoys_Sikell)
# FOURTH GENERATION
circle = personAttributes("Circle", "the Fish", 19, 24, 16, 19, 10, "Male", 0, 0, 0, pi, radius)
diameter = personAttributes("Diameter", "Polygon", 24, 24, 15, 10, 10, "Female", 0, 0, 0, pi, radius)

# this is Dab and Shif and family
starla = personAttributes("Starla", "the Fish", 6, 8, 15, 16, 6, 'Female', 'teal', 'teal', 'sea blue', None, None)
dan = personAttributes("Dan", "the Fish", 19, 1, 7, 6, 4, 'Male', 'black', 'white', 'bright orange', None, None)
dab = personAttributes("Dab", "the Fish", 19, 1, 7, 16, 2, "Male", 'lemon yellow', 'bubblegum-pink', 'bubblegum-pink',
                       starla, dan)
shif = personAttributes("Shif", "the Fish", 19, 32, 15, 14, 12, "Female", 'pale orange', 'soft pink', 'neon pink',
                        starla, dan)

# These are the other fish
# Your Kingdom
arco = personAttributes('Arco', 'the Fish', 13, 16, 17, 18, 14, 'Male', 'light gray', 'dark gray', 'ice blue', None, None)
# Arco is a one-finned fish with a passion for war strategems.
pizzicato = personAttributes('Pizzicato', 'the Fish', 8, 18, 15, 17, 6, 'Female', 'jet black', 'light gray', 'grass green', None, None)
# Pizzicato is a famous fish robber who has never been caught. She steals only Fishian gold.
iodine = personAttributes('Iodine', 'the Fish', 15, 19, 16, 12, 30, 'Female', 'white', 'vermillion', 'sea blue', None, None)
# Iodine is a fish who has a knack for the Art of Fishcromancy.
# Cloud Mountains
koyden = personAttributes('Köyden', 'the Fish', 16, 36, 19, 12, 14, 'Female', 'twilight', 'sky blue', 'mint green', None, None)
# Köyden is a fish known for her hardy and rushing battle strategy. She has killed many fish.
silicon = personAttributes('Silicon', 'the Fish', 17, 13, 32, 14, 18, 'Female', 'soft gray-white', 'light gray', 'forest green', None, None)
# Silicon is known across the land for her skill in Python programming.
endurance = personAttributes('Endurance', 'the Fish', 11, 12, 5, 9, 7, 'Male', 'dark brown', 'white', 'sunrise', None, None)
# Endurance is a young fish who loves stargazing atop snowy peaks.

# Main functions
def createMoreFish(myFName, myLName, myGenetics, doIPrint):
    myFish = myGenetics.firstname + " " + myGenetics.lastname
    fishArray[myFish] = myGenetics
    if (doIPrint):
        print(fishArray)
def determineValue(femaleValue, maleValue):
    if (isinstance(femaleValue, int)) and (isinstance(maleValue, int)):
        print("They are ints")
        if femaleValue != maleValue:
            print("They the same. Yok")
            return max(femaleValue, maleValue)
        else:
            print("They the same")
            return femaleValue
    elif (not isinstance(femaleValue, int) and not isinstance(maleValue, int)):
        print("Oh my! One!")
        return 1
    else:
        print("A coocl value.")
        return int(femaleValue * maleValue)
def determineGender(maleGenetic):
    # print(maleGenetic)
    if maleGenetic == "X":
        return "Female"
    else:
        return "Male"
def determineColor(femaleColor, maleColor):
    randColor = random.choice(colors)
    possColors = [femaleColor, maleColor, randColor]
    return random.choice(possColors)
def makeoffspring(femaleGenetics, maleGenetics):
    femaleFemaleGenes = femaleGenetics.momGenetics
    femaleMaleGenes = femaleGenetics.dadGenetics
    maleFemaleGenes = maleGenetics.momGenetics
    maleMaleGenes = maleGenetics.dadGenetics
    femaleSTR = [femaleFemaleGenes.strength, femaleMaleGenes.strength]
    maleSTR = [maleFemaleGenes.strength, maleMaleGenes.strength]
    STRpair = [random.choice(femaleSTR), random.choice(maleSTR)]
    femaleINT = [femaleFemaleGenes.intelligence, femaleMaleGenes.intelligence]
    maleINT = [maleFemaleGenes.intelligence, maleMaleGenes.intelligence]
    INTpair = [random.choice(femaleINT), random.choice(maleINT)]
    femaleAGL = [femaleFemaleGenes.agility, femaleMaleGenes.agility]
    maleAGL = [maleFemaleGenes.agility, maleMaleGenes.agility]
    AGLpair = [random.choice(femaleAGL), random.choice(maleAGL)]
    femaleCHR = [femaleFemaleGenes.charisma, femaleMaleGenes.charisma]
    maleCHR = [maleFemaleGenes.charisma, maleMaleGenes.charisma]
    CHRpair = [random.choice(femaleCHR), random.choice(maleCHR)]
    femaleINS = [femaleFemaleGenes.instinct, femaleMaleGenes.instinct]
    maleINS = [maleFemaleGenes.instinct, maleMaleGenes.instinct]
    INSpair = [random.choice(femaleINS), random.choice(maleINS)]
    offspring = personAttributes(str(input("What is your first name?")), maleGenetics.lastname,
                                 determineValue(STRpair[0], STRpair[1]), determineValue(INTpair[0], INTpair[1]),
                                 determineValue(AGLpair[0], AGLpair[1]), determineValue(CHRpair[0], CHRpair[1]),
                                 determineValue(INSpair[0], INSpair[1]), determineGender(maleGenetics.gender),
                                 determineColor(femaleGenetics.bodyColor, maleGenetics.bodyColor),
                                 determineColor(femaleGenetics.finColor, maleGenetics.finColor),
                                 determineColor(femaleGenetics.eyeColor, maleGenetics.eyeColor), femaleGenetics,
                                 maleGenetics)
    return offspring

# Tutorial/Storyline functions
def start():
    print("""Long, long ago, there were two fish...
This is a intricate story, a plot soon to unravel.
And this story starts with you.""")
    print(" ")
    print(" ")
    urMom1 = personAttributes("Unknown", "the Fish", 6, 8, 15, 16, 6, 'Female', 'teal', 'teal', 'sea blue', None, None)
    urMom2 = personAttributes("Unknown", "the Fish", 19, 1, 7, 6, 4, 'Male', 'black', 'white', 'bright orange', None,
                              None)
    urDad1 = personAttributes("Unknown", "the Fish", 8, 9, 17, 3, 8, "Female", "coral pink", "neon pink", "twilight",
                              None, None)
    urDad2 = personAttributes("Unknown", "the Fish", 12, 9, 12, 10, 7, "Male", 'forest green', "grass green",
                              'sky blue', None, None)
    urMom = personAttributes("Unknown", "the Fish", 19, 32, 15, 14, 12, "Female", 'pale orange', 'soft pink',
                             'neon pink', urMom1, urMom2)
    urDad = personAttributes("Unknown", "the Fish", 12, 9, 17, 10, 8, 'Male', 'coral pink', 'vermillion', 'sky blue',
                             urDad1, urDad2)
    urGenes = makeoffspring(urMom, urDad)
    urName = urGenes.firstname
    createMoreFish(urName, "the Fish", urGenes, False)
    urFullName = urName + " the Fish"
    print(" ")
    print(" ")
    if urGenes.gender == 'Female':
        noun = 'girl'
    else:
        noun = 'boy'
    print("You are a young "+noun+", at around 14 years old.")
    print("Your name is " + urFullName + ".")
    print("You have a strength value of " + str(urGenes.strength) + ".")
    print("Your intelligence is " + str(urGenes.intelligence) + ", ")
    print("and your agility value is " + str(urGenes.agility) + ".")
    print("Your charisma(good looks) is " + str(urGenes.charisma) + ".")
    print("And finally your instinct value is " + str(urGenes.instinct) + ". ")
    print("This is how good you are at casting spells.")
    print("You have "+ urGenes.finColor +" hair and you like wearing "+ urGenes.bodyColor +" clothes.")
    print("Your eyes are " + urGenes.eyeColor + ".")
    return urName, urFullName

print(title)
gameStart = input('Play? (y/n) ')
if gameStart == 'y':
    urName, urFullName = start()
