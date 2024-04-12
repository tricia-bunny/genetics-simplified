import random

title = "Genetics: Oversimplified"
# genetics = [strength, intelligence, agility, charisma, instinct, sex]
numlist = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0.5, 1.5,
           2.0]
genlist = ["X", "Y"]
gendlist = ["Male", "Female"]
colors = ['crimson', 'carmine', 'vermillion', 'bright orange', 'pale orange', 'orange-yellow', 'sunrise yellow',
          'lemon yellow', 'yellow-green', 'lime green', 'mint green', 'grass green', 'forest green', 'dark teal',
          'teal', 'sea blue', 'ice blue', 'sky blue', 'twilight', 'parma', 'imperial violet', 'jet black', 'dark brown',
          'dark gray', 'light gray', 'soft gray-white', 'white', 'baby pink', 'soft pink', 'bubblegum-pink',
          'neon pink', 'coral pink']

from collections import namedtuple

personAttributes = namedtuple('personAttributes',
                              'firstname, lastname, strength, intelligence, agility, charisma, instinct, gender, bodyColor, finColor, eyeColor, momGenetics, dadGenetics')
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


def assignXY(Map, x, y, string):
    myFishLand = Map.copy()
    # for i in Map:
    #    myFishLand.append(list(i))
    mylist = list(myFishLand[y + 1])
    mylist[x + 3] = string
    myFishLand[y + 1] = ''.join(mylist)
    return myFishLand


def printMap(theMap):
    num = 0
    for i in theMap:
        num += 1
        print(theMap[num - 1])


def printDict(theDict):
    toBePrinted = list(theDict.items())
    num = 0
    for i in toBePrinted:
        num += 1
        print(toBePrinted[num - 1])


def addFish(theArray, theFish):
    fishName = theFish.firstname + " " + theFish.lastname
    theArray[fishName] = theFish


fishcromancerStratagems = ['Stab', 'Slash', 'Ambush', 'Un-Mutate', 'Raise the Dead']
normalStratagems = ['Stab', 'Slash', 'Ambush', 'Sweep']


def createStratagemList(num, stratagems):
    stratagemList = []
    for i in range(num):
        stratagemList.append(random.choice(stratagems))
    return stratagemList


normalEnemyStratagems = createStratagemList(200, normalStratagems)
fishcromancerEnemyStratagems = createStratagemList(400, fishcromancerStratagems)

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
scalene = personAttributes("Scalene", "the Fish", 16, 24, 15, 29, 8, "Male", 'light gray', 'dark gray', 'hazel', perimeter, area)
isosceles = personAttributes("Isosceles", "Polygon", 19, 12, 15, 1, 20, "Female", 'forest green', 'carmine', 'ice blue', angle, degree)
# SECOND GENERATION
kale = personAttributes("Kale", "the Fish", 19, 8, 9, 19, 19, "Female", 'grass green', 'mint green', 'twilight', fidget,
                        bob)
triangle = personAttributes("Triangle", "Polygon", 19, 12, 15, 1, 10, "Male", 'light gray', 'pale yellow', 'ice blue', isosceles, scalene)
radius = personAttributes("Radius", "Polygon", 19, 12, 15, 10, 10, "Male", 'vermillion', 'carmine', 'hazel', isosceles, scalene)
# THIRD GENERATION
fish = personAttributes("Fish", "the Fish", 29, 38, 16, 19, 19, "Male", 0, 0, 0, kale, theBoys_Sikell)
pi = personAttributes("π", "the Fish", 29, 38, 16, 19, 10, "Female", 0, 0, 0, kale, theBoys_Sikell)
# FOURTH GENERATION
circle = personAttributes("Circle", "the Fish", 19, 24, 16, 19, 10, "Male", 0, 0, 0, pi, radius)
diameter = personAttributes("Diameter", "Polygon", 24, 24, 15, 10, 10, "Female", 0, 0, 0, pi, radius)
# This is our aquarium
fidgetFamilyArray = {}
addFish(fidgetFamilyArray, fidget)
addFish(fidgetFamilyArray, theBoys_Sikell)
addFish(fidgetFamilyArray, bob)
addFish(fidgetFamilyArray, kale)
addFish(fidgetFamilyArray, fish)
addFish(fidgetFamilyArray, pi)
addFish(fidgetFamilyArray, scalene)
addFish(fidgetFamilyArray, isosceles)
addFish(fidgetFamilyArray, triangle)
addFish(fidgetFamilyArray, radius)
addFish(fidgetFamilyArray, circle)
addFish(fidgetFamilyArray, diameter)
# our aquarium: fidgetFamilyArray
# to view aquarium delete the "#" in next line
# print(fidgetFamilyArray)

# this is Dab and Shif and family
starla = personAttributes("Starla", "the Fish", 6, 8, 15, 16, 6, 'Female', 'teal', 'teal', 'sea blue', None, None)
dan = personAttributes("Dan", "the Fish", 19, 1, 7, 6, 4, 'Male', 'black', 'white', 'bright orange', None, None)
dab = personAttributes("Dab", "the Fish", 19, 1, 7, 16, 2, "Male", 'lemon yellow', 'bubblegum-pink', 'bubblegum-pink',
                       starla, dan)
shif = personAttributes("Shif", "the Fish", 19, 32, 15, 14, 12, "Female", 'pale orange', 'soft pink', 'neon pink',
                        starla, dan)

'''
#These are the other fish
#Your Kingdom
arco = personAttributes('Arco', 'the Fish', 13, 16, 17, 18, 14, 'Male', 'light gray', 'dark gray', 'ice blue')
#Arco is a one-finned fish with a passion for war strategems.
pizzicato = personAttributes('Pizzicato', 'the Fish', 8, 18, 15, 17, 6, 'Female', 'jet black', 'light gray', 'grass green')
#Pizzicato is a famous fish robber who has never been caught. She steals only Fishian gold.
iodine = personAttributes('Iodine', 'the Fish', 15, 19, 16, 12, 30, 'Female', 'white', 'vermillion', 'sea blue')
#Iodine is a fish who has a knack for the Art of Fishcromancy.
#Cloud Mountains
koyden = personAttributes('Köyden', 'the Fish', 16, 36, 19, 12, 14, 'Female', 'twilight', 'sky blue', 'mint green')
#Köyden is a fish known for her hardy and rushing battle strategy. She has killed many fish.
silicon = personAttributes('Silicon', 'the Fish', 17, 13, 32, 14, 18, 'Female', 'soft gray-white', 'light gray', 'forest green')
#Silicon is known across the land for her skill in Python programming.
endurance = personAttributes('Endurance', 'the Fish', 11, 12, 5, 9, 7, 'Male', 'dark brown', 'white', 'sunrise')
#Endurance is a young fish who loves stargazing atop snowy peaks.
'''


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


def makeOffspring(names, genetics):
    offspring = [0, 0, 0, 0, 0, "NaG"]
    # strength
    offspring[0] = determineValue(genetics[0], genetics[1])
    # intelligence
    offspring[1] = determineValue(genetics[2], genetics[3])
    # agility
    offspring[2] = determineValue(genetics[4], genetics[5])
    # charisma
    offspring[3] = determineValue(genetics[6], genetics[7])
    # instinct
    offspring[4] = determineValue(genetics[8], genetics[9])
    # gender
    offspring[5] = determineGender(genetics[11])

    return offspring


def make_Offspring(femaleGenetics, maleGenetics):
    offspring = personAttributes(str(input("What is the name of your fish offspring?")), maleGenetics.lastname,
                                 determineValue(femaleGenetics.strength, maleGenetics.strength),
                                 determineValue(femaleGenetics.intelligence, maleGenetics.intelligence),
                                 determineValue(femaleGenetics.agility, maleGenetics.agility),
                                 determineValue(femaleGenetics.charisma, maleGenetics.charisma),
                                 determineValue(femaleGenetics.instinct, maleGenetics.instinct),
                                 determineGender(maleGenetics.gender),
                                 determineColor(femaleGenetics.bodyColor, maleGenetics.bodyColor),
                                 determineColor(femaleGenetics.finColor, maleGenetics.finColor),
                                 determineColor(femaleGenetics.eyeColor, maleGenetics.eyeColor))
    """
    first_name = input("What is the name of your fish offspring?")
    offspring.firstname = first_name
    offspring.firstname = str(input("What is the name of your fish offspring?"))
    offspring.lastname = maleGenetics.lastname
    #strength
    offspring.strength = determineValue(femaleGenetics.strength, maleGenetics.strength)
    #intelligence
    offspring.intelligence = determineValue(femaleGenetics.intelligence, maleGenetics.intelligence)
    #agility
    offspring.agility = determineValue(femaleGenetics.agility, maleGenetics.agility)
    #charisma
    offspring.charisma = determineValue(femaleGenetics.charisma, maleGenetics.charisma)
    #instinct
    offspring.instinct = determineValue(femaleGenetics.instinct, maleGenetics.instinct)
    #gender
    offspring.gender = determineGender(maleGenetics.gender)
    """

    return offspring


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
    offspring = personAttributes(str(input("What is the name of your fish?")), maleGenetics.lastname,
                                 determineValue(STRpair[0], STRpair[1]), determineValue(INTpair[0], INTpair[1]),
                                 determineValue(AGLpair[0], AGLpair[1]), determineValue(CHRpair[0], CHRpair[1]),
                                 determineValue(INSpair[0], INSpair[1]), determineGender(maleGenetics.gender),
                                 determineColor(femaleGenetics.bodyColor, maleGenetics.bodyColor),
                                 determineColor(femaleGenetics.finColor, maleGenetics.finColor),
                                 determineColor(femaleGenetics.eyeColor, maleGenetics.eyeColor), femaleGenetics,
                                 maleGenetics)
    return offspring


battleStratagems = {
    'Stab': 'Stab the enemy',  # 7% chance of dodge
    'Slash': 'Slash at the enemy',  # 13% chance of dodge
    'Ambush': 'Ambush the enemy',  # 30% chance of dodge, 30% ch of crit
    'Sweep': 'Sweep sword below enemy',  # 50% chance of dodge, 40% ch of crit
    '360 Degree Slash': 'Spin in a complete circle, slashing all around you.', # 70% chance of dodge, 100% chance of crit
    'Un-Mutate': 'Something only fish-necromancers can do. Turns an undead fish into a live one.',  # 0% ch of evryding
    'Raise the Dead': '''Something only fishcromancers can do. Raises the spirits of 5 dead fish to attack...but they m
    ay attack you''',  # 70% chance of crit
}
stabDodgeChance, stabCritChance = 7, 0
slashDodgeChance, slashCritChance = 13, 0
ambushDodgeChance, ambushCritChance = 30, 30
sweepDodgeChance, sweepCritChance = 50, 40
_360DodgeChance, _360CritChance = 85, 100

def Attack(attackDodgeChance, attackCritChance, firstFishStats, secondFishStats, secondFishHP, attacker, attacked, attackType):
    if attackType == 'Ambush':
        extraS = 'e'
    else:
        extraS = ''

    if attackType == 'Stab':
        motion = 'stab' + extraS + ' towards'
    elif attackType == 'Slash' or attackType == '360 Degree Slash':
        motion = 'slash' + extraS + ' towards'
    elif attackType == 'Ambush':
        motion = 'ambush' + extraS
    elif attackType == 'Sweep':
        motion = 'sweep' + extraS + ' towards'

    print(attacker + ' ' + motion + ' ' + attacked + '...')
    dodgeChance = secondFishStats.agility + attackDodgeChance
    chance = random.randint(0, 100)
    if chance <= dodgeChance:
        print('...and ' + attacked + ' dodge' + extraS + ' it!')
    else:
        print('...and the attack connects!')
        critChance = random.randint(0, 100)
        attackDamage = firstFishStats.strength
        criticalChance = firstFishStats.intelligence + attackCritChance
        if critChance <= criticalChance:
            print('It is a critical hit!!!')
            attackDamage *= 2
        secondFishHP -= attackDamage
    return secondFishHP


def unMutate(secondFishStats, secondFishHP, secondFishCap, attacker):
    if attacker != 'You':
        extraS = 's'
        attacked = 'you'
        somethingR = 'thei'
        pronoun = 'is'
    else:
        extraS = ''
        attacked = 'the fish'
        somethingR = 'you'
        pronoun = 'are'
    print(attacker + ' raise' + extraS + ' ' + somethingR + 'r fins in a Fishcromancer stance.')
    print('Nyaa! ' + attacker + ' shout' + extraS + '.')
    if (secondFishStats.intelligence == 0) and (secondFishStats.instinct == 0):
        # The target is mutated
        print("A beam of arcing blue light shoots from " + somethingR + "r interlaced fins.")
        print(attacked + ' ' + pronoun + ' no longer mutated.')
        nextPeepGenes = secondFishStats
        secFishStats = personAttributes(nextPeepGenes.firstname, nextPeepGenes.lastname, nextPeepGenes.strength,
                                        random.randint(5, 10), nextPeepGenes.agility, nextPeepGenes.charisma,
                                        random.randint(2, 6), nextPeepGenes.gender, nextPeepGenes.bodyColor,
                                        nextPeepGenes.finColor, nextPeepGenes.eyeColor, nextPeepGenes.momGenetics,
                                        nextPeepGenes.dadGenetics)

    else:
        print("A beam of arcing blue light shoots from " + somethingR + "r interlaced fins.")
        print('It sputters and fades.')
        print('\'What the heck?\' ' + attacker + ' exclaim' + extraS + '.')
        secondFishHP *= 1.5
        secondFishHP = int(secondFishHP)
        if secondFishHP > secondFishCap:
            secondFishHP = secondFishCap
        secFishStats = secondFishStats
    return secondFishHP, secFishStats


def raiseDead(firstFishStats, secondFishStats, secondFishHP, firstFishHP, attacker, xenon, angle, cashmere):
    tuple_fish = personAttributes('Tuple', 'the Fish', 8, 9, 17, 16, 7, 'Male', 'coral pink', 'bright orange',
                                  'neon pink',
                                  None, None)
    iridium = personAttributes("Iridium", 'the Fish', 19, 9, 12, 16, 8, 'Female', 'pale orange', 'orange yellow',
                               'carmine',
                               None, None)
    lithium = personAttributes("Angle", 'the Fish', 12, 9, 15, 10, 17, 'Female', 0, 0, 0, None, None)
    deadFish = [tuple_fish, xenon, angle, cashmere, iridium, lithium]
    possAttacks = ['Stab', 'Slash', 'Ambush', 'Sweep']
    chosenFish = []
    if attacker == 'You':
        extraS = ' '
    else:
        extraS = 's'
    print('A splatter of blue sparks showers into the sky.')
    print('And then the likeness of a fish rises out of the mist.')
    for i in range(5):
        chosenfish = random.choice(deadFish)
        chosenFish.append(chosenfish)
        print('It is ' + chosenfish.firstname + "!")
    for i in chosenFish:
        atatck = random.choice(possAttacks)
        if random.randint(0, 4) <= 1:
            stats1 = firstFishStats
            stats2 = secondFishStats
            hp = secondFishHP
            attacked = 'the fish'
        else:
            stats1 = secondFishStats
            stats2 = firstFishStats
            hp = firstFishHP
            attacked = 'you'
        returnedHP = Attack(0, 70, stats1, stats2, hp, i.firstname, attacked, atatck)
        if hp == firstFishHP:
            firstFishHP = returnedHP
        else:
            secondFishHP = returnedHP
    return secondFishHP, firstFishHP


def simulateAttack(attacker, attack, firstFishStats, secondFishStats, firstFishHP, secondFishHP, secondFishCap):
    if attacker != 'You':
        attacked = 'you'
    else:
        attacked = 'the fish'
    breakForUnMutation = False
    if attack == 'Stab':
        dodgeChance, critChance = stabDodgeChance, stabCritChance
    elif attack == 'Slash':
        dodgeChance, critChance = slashDodgeChance, slashCritChance
    elif attack == 'Ambush':
        dodgeChance, critChance = ambushDodgeChance, ambushCritChance
    elif attack == 'Sweep':
        dodgeChance, critChance = sweepDodgeChance, sweepCritChance
    if attack != 'Un-Mutate' and attack != 'Raise the Dead' and attack != '360 Degree Slash':
        secondFishHP = Attack(dodgeChance, critChance, firstFishStats, secondFishStats, secondFishHP, attacker, attacked, 
                              attack)
    elif attack == '360 Degree Slash':
        for i in range(random.randint(2, 10)):
            secondFishHP = Attack(_360DodgeChance, _360CritChance, firstFishStats, secondFishStats, secondFishHP, attacker, attacked, attack)
    elif attack == 'Un-Mutate':
        secondFishHP, secFishStats = unMutate(secondFishStats, secondFishHP, secondFishCap, attacker)
        if secondFishStats != secFishStats:
            if attacker == 'You':
                attacked = 'The fish'
                pronoun = 'has been'
            else:
                attacked = 'You'
                pronoun = 'were'
            print(attacked + ' ' + pronoun + ' un-mutated!')
            breakForUnMutation = True
    elif attack == 'Raise the Dead':
        secondFishHP, firstFishHP = raiseDead(firstFishStats, secondFishStats, secondFishHP, firstFishHP, attacker, xenon, angle, cashmere)

    return firstFishHP, secondFishHP, breakForUnMutation


def battle(firstFishStats, firstFishHP, firstFishCap, secondFishStats, secondFishHP, secondFishCap, enemyStratagems):
    # Strength (xxxFishStats.strength) is the dealt damage. It tastes like
    # Intelligence is the probability that the dealt attack is a crit hit. It tastes like ginger lemon chews.
    # Agility is the probability that the attack will be dodged. It tastes like
    # Charisma does nothing. It tastes like fishflower nectar.
    # Instinct is for casting spells. It tastes like cherry blossoms and fishes' blood.
    # First fish(you) always goes first
    print('It is time for a battle!')
    print('These are the attacks you can use!')
    printDict(battleStratagems)
    yourturn = True
    numStratagem = 0
    while firstFishHP > 0 and secondFishHP > 0:
        attack = "  "
        if yourturn == True:
            while attack not in battleStratagems.keys():
                attack = input('What kind of attack do you want to do? (Enter in full.)')
            attacker = 'You'
            firstFishHP, secondFishHP, breakForUnMutation = simulateAttack(attacker, attack, firstFishStats,
                                                                           secondFishStats, firstFishHP, secondFishHP, secondFishCap)
            yourturn = False
        else:
            attack = enemyStratagems[numStratagem]
            attacker = 'The fish'
            secondFishHP, firstFishHP, breakForUnMutation = simulateAttack(attacker, attack, secondFishStats,
                                                                           firstFishStats, secondFishHP, firstFishHP, firstFishCap)
            yourturn = True
            numStratagem += 1
        if breakForUnMutation == True:
            break
        print('Your health is ' + str(firstFishHP))
        print('The fish\'s health is ' + str(secondFishHP))
    if firstFishHP < 1:
        winner = 'The fish'
        loser = 'you'
    else:
        winner = 'You'
        loser = 'the fish'
    if breakForUnMutation == False:
        print('The battle has ended.')
        print(winner + ' has won.')
    else:
        print('The battle has ended, ')
        print('because ' + loser + " has been un-mutated.")
    return breakForUnMutation, loser


fishArray = {}
missionArray = {}
missionArray['Defeat Dab'] = 'Defeat Dab and save Fishland! Reward: Unknown'
#                                                                   Shif's crystal spearhead
completedMissions = {}
invasionsList = ['Cloud Mountains']
completedInvasions = []
# completedInvasions.append('Peak Depths: Invasion')
fishianGold = 0
fishFood = 0
items = {'A Random Orb': ['orb', 'instinct', 10], 'Fidget\'s Pocketknife': ['weapon', 'knife', 3], 'Fishian Iron': ['material', 'fishian iron', 0], 'Sea Glass': ['material', 'sea glass', 0], 'Wood': ['material', 'wood', 0], 'Coral': ['material', 'coral', 0], 'Stone': ['material', 'stone', 0], 'Mineral': ['material', 'mineral', 0]}
gotGold = False
gotArco = False
metPizz = False
metIodine = False
gotMoreGold = False
borderCrossed = False
guardsDefeated = False
metEndurance = False
gotOrb = False
gotYay = False
metShale = False
valorAsked = False
andesiteRAWR = False
metCinnabar = False
gotIrn = False
yourKingdomStuff = [gotGold, gotArco, metPizz, metIodine]
cloudMountainStuff = [gotMoreGold, borderCrossed, guardsDefeated, metEndurance, gotOrb, gotYay]
mineralValleyStuff = [metShale, valorAsked, andesiteRAWR]
peakDepthsStuff = [metCinnabar, gotIrn]
kingdomStuff = [yourKingdomStuff, cloudMountainStuff, mineralValleyStuff, peakDepthsStuff]


# start of program
def createFish():
    myFName = input("What is the fish's first name?")
    myLName = input("What is the fish's last name?")
    randomValues = input("Do you wish to have random genetic values? (y/n) ")
    if randomValues == "y":
        myGenetics = personAttributes(myFName, myLName, random.choice(numlist), random.choice(numlist),
                                      random.choice(numlist), random.choice(numlist), random.choice(numlist),
                                      random.choice(gendlist), random.choice(colors), random.choice(colors),
                                      random.choice(colors), None, None)
    elif randomValues == "n":
        print("These are your color choices")
        print(colors)
        myGenetics = personAttributes(myFName, myLName, input("Enter " + myFName + "'s Strength value: "),
                                      input("Enter " + myFName + "'s Intelligence value: "),
                                      input("Enter " + myFName + "'s Agility value: "),
                                      input("Enter " + myFName + "'s Charisma value: "),
                                      input("Enter " + myFName + "'s Instinct value: "), random.choice(gendlist),
                                      input("Enter " + myFName + "'s body color: "),
                                      input("Enter " + MyFName + "'s fin color: "),
                                      input("Enter " + myFName + "'s eye color: "), None, None)
    myFish = myGenetics.firstname + " " + myGenetics.lastname
    fishArray[myFish] = myGenetics
    print(fishArray)


def createMoreFish(myFName, myLName, myGenetics, doIPrint):
    myFish = myGenetics.firstname + " " + myGenetics.lastname
    fishArray[myFish] = myGenetics
    if (doIPrint):
        print(fishArray)


def createFromAquarium():
    print("This is your fish:")
    print(fishArray)
    firstPeep = input("Please enter the ENTIRE NAME of the first fish. (If you don't, it will go wrong) ")
    nextPeep = input("Please enter the ENTIRE NAME of the second fish. (If you don't, it will go wrong) ")
    firstPeepGenes = fishArray[firstPeep]
    nextPeepGenes = fishArray[nextPeep]
    if firstPeepGenes.gender == nextPeepGenes.gender:
        print("These fish can't be mated in this version of the game.")
    else:
        if firstPeepGenes.gender == "Female":
            gen = "X"
        else:
            gen = random.choice(genlist)
        firstPeepGenetics = personAttributes(firstPeepGenes.firstname, firstPeepGenes.lastname, firstPeepGenes.strength,
                                             firstPeepGenes.intelligence, firstPeepGenes.agility,
                                             firstPeepGenes.charisma, firstPeepGenes.instinct, gen,
                                             firstPeepGenes.bodyColor, firstPeepGenes.finColor, firstPeepGenes.eyeColor, 
                                            firstPeepGenes.momGenetics, firstPeepGenes.dadGenetics)
        if nextPeepGenes.gender == "Female":
            gen = "X"
        else:
            gen = random.choice(genlist)
        nextPeepGenetics = personAttributes(nextPeepGenes.firstname, nextPeepGenes.lastname, nextPeepGenes.strength,
                                            nextPeepGenes.intelligence, nextPeepGenes.agility, nextPeepGenes.charisma,
                                            nextPeepGenes.instinct, gen, nextPeepGenes.bodyColor,
                                            nextPeepGenes.finColor, nextPeepGenes.eyeColor,
                                            nextPeepGenes.momGenetics, nextPeepGenes.dadGenetics)
        offspring = makeoffspring(firstPeepGenetics, nextPeepGenetics)
        return offspring


def makeNewFish():
    nameFemale = input("Please enter the first name of the mother. (Choose something random) ")
    lnameFemale = input("Please enter the last name of the mother. (Choose something random) ")
    nameMale = input("Please enter the first name of the father. (Choose something random) ")
    lnameMale = input("Please enter the last name of the father. (Choose something random) ")
    randomValues = input("Do you wish to have random genetics values or not? (y/n) ")
    if randomValues == "y":
        # list = [female strength, male strength, female intel, male intel, female agility, male agility...]
        femaleGenetics = personAttributes(nameFemale, lnameFemale, random.choice(numlist), random.choice(numlist),
                                          random.choice(numlist), random.choice(numlist), random.choice(numlist), "X",
                                          random.choice(colors), random.choice(colors), random.choice(colors)), None, None
        maleGenetics = personAttributes(nameMale, lnameMale, random.choice(numlist), random.choice(numlist),
                                        random.choice(numlist), random.choice(numlist), random.choice(numlist),
                                        random.choice(genlist), random.choice(colors), random.choice(colors),
                                        random.choice(colors)), None, None
        # nameList = [nameF, lnameF, nameM, lnameM]
        # geneticsList = [random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), "X", random.choice(genlist)]

    elif randomValues == "n":
        print("These are your color choices")
        print(colors)
        femaleGenetics = personAttributes(nameFemale, lnameFemale, input("Enter " + nameFemale + "'s Strength value: "),
                                          input("Enter " + nameFemale + "'s Intelligence value: "),
                                          input("Enter " + nameFemale + "'s Agility value: "),
                                          input("Enter " + nameFemale + "'s Charisma value: "),
                                          input("Enter " + nameFemale + "'s Instinct value: "), "X",
                                          input("Enter " + nameFemale + "'s body color: "),
                                          input("Enter " + nameFemale + "'s fin color: "),
                                          input("Enter " + nameFemale + "'s eye color: "), None, None)
        maleGenetics = personAttributes(nameMale, lnameMale, input("Enter " + nameMale + "'s Strength value: "),
                                        input("Enter " + nameMale + "'s Intelligence value: "),
                                        input("Enter " + nameMale + "'s Agility value: "),
                                        input("Enter " + nameMale + "'s Charisma value: "),
                                        input("Enter " + nameMale + "'s Instinct value: "), random.choice(genlist),
                                        input("Enter " + nameMale + "'s body color: "),
                                        input("Enter " + nameMale + "'s fin color: "),
                                        input("Enter " + nameMale + "'s eye color: "), None, None)

        # geneticsList = [input("Enter "+nameFemale+"'s Strength value: "), input("Enter "+nameMale+"'s Strength value: "), input("Enter "+nameFemale+"'s Intelligence value: "), input("Enter "+nameMale+"'s Intelligence value: "), input("Enter "+nameFemale+"'s Agility value: "), ]

    print("Your aquarium:")
    femaleGenes = personAttributes(nameFemale, lnameFemale, femaleGenetics.strength, femaleGenetics.intelligence,
                                   femaleGenetics.agility, femaleGenetics.charisma, femaleGenetics.instinct, "Female",
                                   femaleGenetics.bodyColor, femaleGenetics.finColor, femaleGenetics.eyeColor, None, None)
    maleGenes = personAttributes(nameMale, lnameMale, maleGenetics.strength, maleGenetics.intelligence,
                                 maleGenetics.agility, maleGenetics.charisma, maleGenetics.instinct, "Male",
                                 maleGenetics.bodyColor, maleGenetics.finColor, maleGenetics.eyeColor, None, None)
    createMoreFish(nameFemale, lnameFemale, femaleGenes, False)
    createMoreFish(nameMale, lnameMale, maleGenes, True)
    print("Your randomly generated Genetic offspring is: ")
    offspring = make_Offspring(femaleGenetics, maleGenetics)
    print(offspring)
    createMoreFish(offspring.firstname, offspring.lastname, offspring, True)


def testprogram():
    femaleGenetics = personAttributes("Soy", "Bean", 2, 2, 3, 0.5, 12, "X", 'coral pink', 'sky blue', 'ice blue')
    maleGenetics = personAttributes("Bean", "the Fish", 2, 4, 6, 2.0, 12, "Y", 'grass green', 'forest green',
                                    'jet black')
    print("Your randomly generated Genetic offspring is: ")
    offspring = make_Offspring(femaleGenetics, maleGenetics)
    assert (offspring.firstname == "Soybean")
    assert (offspring.lastname == "the Fish")
    assert (offspring.strength == 2)
    assert (offspring.intelligence == 4)
    assert (offspring.agility == 6)
    assert (offspring.charisma == 1)
    assert (offspring.instinct == 12)
    assert (offspring.gender == "Male")


# Game

radiusflashback = '''
>Flashback<
You, Pi, and Triangle were on a small patrol to aid the rebelling Coral
Shallows fish against Dab's army. 
"Pi..?" Triangle had whispered upon seeing a vermillion fish with carmine
fins and blazing hazel eyes.
"Triangle? What's wrong?" Pi had asked.
When Dab's army charged, you'd seen the vermillion fish's eyes
go wide upon seeing the threesome. "Triangle!" he had shouted.
Triangle froze, then ran faster than a tumblekelp. "Radius!"
Then Dab screamed. "Radius, you insolent fish! Kill him!"
Radius looked from Triangle to Dab then back to Triangle. "I'm sorry, Triangle..."
A fish suddenly came at you, and when the fight was over you saw Triangle
sprawled on the ground, with Radius standing over him.
Pi pushed Radius over, leapt for Dab and scratched his
right fin-tendon uber-lightly with her knife.
"Retreat!" Dab yelled in pain. Picking up Radius with his RIGHT 
fin, he throws him towards a twilight fish. The twilight fish had 
grabbed him and off Dab's army went.
'''

def adventure(x, y):
    x += 3
    y += 1
    if x <= 2:
        place = None
    if x == 3:
        if y == 6:
            place = 'Upper Flat Isle'
        elif y == 7:
            place = 'Coral Beach'
        elif y == 8:
            place = 'Lower Flat Isle'
        else:
            place = None
    elif x == 4:
        if y == 6:
            place = 'Inner Flat Isle'
        elif y == 7:
            place = 'Coral Cliffs'
        elif y == 8:
            place = 'Flat Isle Trails'
        elif y == 10:
            place = 'Upper Glass Coast'
        elif y == 11:
            place = 'Lower Glass Coast'
        else:
            place = None
    elif x == 5:
        if y == 2:
            place = 'Frost'
        elif y == 3:
            place = 'Lower Frost'
        elif y == 5:
            place = 'Sea Salt Shore'
        elif y == 6:
            place = 'Flat Ridge'
        elif y == 7:
            place = 'Coral Highlands'
        elif y == 8:
            place = 'Inner Flat Isle Trails'
        elif y == 9:
            place = 'Glass Drop'
        elif y == 10:
            place = 'Glass Slope'
        elif y == 11:
            place = 'Glass Flatlands'
        elif y == 12:
            place = 'Sand Dollar Valley'
        else:
            place = None
    elif x == 6:
        if y == 2:
            place = 'Inner Frost'
        elif y == 3:
            place = 'Lower Frostland'


adventurePlaces = {'@': 'Frost', 'b': 'Kelp Ridge', 'f': 'Dabdom', '=': 'Ignia', '#': 'Sandy Plains',
                   'o': 'Astatine Hills', 'k': 'Coral Shallows', '*': 'Grain Flatlands', '%': 'Blossom',
                   'l': 'Skyfish Coast', 's': 'Sea-Glass Cliffs', 't': 'Your Kingdom', 'q': 'Peak Depths',
                   '$': 'Mineral Valley', ':': 'Carrot Highlands', 'e': 'Starfish Bluff', 'j': 'Echo Caverns',
                   '&': 'Sky Shore', '^': 'Cloud Mountains', ' ': None}


def findPlace(x, y):
    y += 3
    x += 1
    place = adventurePlaces[fishMap[y][x]]
    print(fishMap[y][x])
    print(fishMap[y - 3][x - 1])
    return place


adventuring = {
    'Frost': '''Frost is a place of icy coldness.
    The snow-studded peaks reach high above the clouds.''',
    'Kelp Ridge': '''Kelp Ridge: A beautiful place with sprawling
    beaches and fish and kelp. It is warm and sunny always.''',
    'Dabdom': '''Dabdom is where Dab rules supreme.
    It is a place with many ferocious guards, and legends tell of fishcromancy...''',
    'Ignia': '''Ignia, a place so hot that only the most hardy fish can survive.
    Legends tell of a network of underground tunnels leading to anywhere you want.''',
    'Sandy Plains': '''Covered in layers upon layers of fine white sand,
    these plains grow only the scarcest of corals and kelps.''',
    'Astatine Hills': '''Beneath the grassy surface lays tonnes of Astatine:
    A element that can kill fish...and much worse.''',
    'Coral Shallows': '''Fin-deep wading pools littered around this land contain
    beautiful coral clusters. A coppery sand surrounds them.''',
    'Grain Flatlands': '''The main source of food production, the fish here grow
    many types of grain, millet, and oat. They sell it at impossibly low prices.''',
    'Blossom': '''Blossom, a place where cherry blossoms bloom year-round.
    We still haven't figured out how they do it. Oh well.''',
    'Skyfish Coast': '''A serene sea town where Sky fish reside.
    Look closely and wait, for they can tell your future.''',
    'Sea-Glass Cliffs': '''Sea Glass lays embedded in these towering cliffs.
    A big enough piece could buy you all of the Fishian land!''',
    'Your Kingdom': '''Your kingdom where you reign. You wouldn't want to
    explore here. It's too boring here...''',
    'Peak Depths': '''The deepest point of Fishland, no fish dares
    to explore here. Many a good fish has gone missing here.''',
    'Mineral Valley': '''Rich deposits of salt and mineral are buried here.
    With just the right amount of luck, even the poorest fish could strike it rich.''',
    'Carrot Highlands': '''Carrots grow in these humid conditions,
    planted by diligent farmer fishes and their family.''',
    'Starfish Bluff': '''Starfish reside in this dreary, gray region.
    Listen to their call: They will show you the way to success.''',
    'Echo Caverns': '''Lost fish in these neverending caves yell for help,
    yet their calls still reverbrate in these caverns. Will they ever get out?''',
    'Sky Shore': '''Along this shore there are great stargazing points.
    The fish here say, from here you can read the will of the skies.''',
    'Cloud Mountains': '''These snow-glazed mountains peak high into the clouds.
    It is heard that a legendary fishcromancer resides here, between the earth and the skies.''',
}


def fishAdventure(place, urName):
    FishArray = fishArray
    print('You have arrived in ' + place + '!')
    input('Press enter to continue. ')
    print(adventuring[place])
    print(' ')
    print(list(FishArray))
    peeps = [urName]
    onePeep = ' '
    print('Which fish do you want to bring on this expedition?')
    print('You can bring up to 5 fish, including you. You must be the leader.')
    while True:
        adventureLeader = input('Who is the secondary leader of this adventure? \n (Enter the FULL NAME of the fish.) ')
        if (adventureLeader in list(FishArray)) and (not adventureLeader in peeps):
            print(adventureLeader + ' is qualified to be the leader.')
            peeps.append(adventureLeader)
            break
        else:
            print('This fish does not exist, or is already in the mission!')
    for i in range(4):
        if onePeep.lower == 'n':
            break
        while True:
            onePeep = input('Who is another fish you want to bring? If there is no, enter "n".')
            if (onePeep in list(FishArray)) and (not onePeep in peeps):
                print(onePeep + ' is qualified to be on this mission.')
                peeps.append(onePeep)
                break
            elif onePeep.lower() == 'n':
                break
            else:
                print('This fish does not exist, or is already in the mission!!')
    print('Your mission team: \n' + str(peeps))
    return peeps


def meetArco(Team, gotArco):
    print('Your team comes out into a grassy clearing.')
    print('There is a small, intricate sea glass knife hidden by the brush.')
    print('You look closely...and see that a fish has snuck up behind you!')
    print('The fish is light gray with dark gray fins and brilliant ice blue eyes.')
    if 'Pizzicato the Fish' not in Team:
        print('The fish asks, \'Are you with Dab?\'')
        print('You reply, \'No\'.')
        print('Then he replies: \'Beat me in a duel...and I will join you.\'')
        arco = personAttributes('Arco', 'the Fish', 13, 16, 17, 18, 14, 'Male', 'light gray', 'dark gray', 'ice blue',
                                None, None)
        '''
        print('To beat the fish, a fish must have at least 13 strength and 17 agility to beat the fish.')
        losses = 0
        for i in Team:
            if (fishArray[i].strength >= 13) and (fishArray[i].agility >= 17):
                print(i+' has defeated the fish in a duel!')
                break
            else:
                print(i+' could not win, and is heavily wounded.')
                losses += 1
        if losses == len(Team):
            print('The fish has defeated all. Sadly you retreat back to the safety of your camp.')
            print('\'Ha! You couldn\'t defeat a lowly fish like me, how will you be able to defeat Dab?\'')
        else:
            print('The fish decides to join your team!')
            print('\'Okay, fine. You beat me.\'')
            print('\'Another step towards the defeat of that horrendous tyrant.\'')
            addFish(fishArray, arco)
        '''
        for i in Team:
            print(i+' steps up: \'You better watch out: I\'ll demolish you!\'')
            nothing, loser = battle(fishArray[i], 200, 200, arco, 120, 120, normalEnemyStratagems)
            if loser == 'the fish': break
        if loser == 'you':
            print('The fish has defeated all. Sadly you retreat back to the safety of your camp.')
            print('\'If you can\'t even defeat me, don\'t even think of taking on Dab!\'')
            print('\'Wait, who are you? You\'re somehow familiar.\' ' + Team[len(Team)-1] + ' says.')
            print('\'I am Arco. Arco of Kelp Ridge.\'')
        else:
            print(i + ' has defeated the fish!')
            print('\'Wait, who are you? You\'re somehow familiar.\' ' + Team[len(Team)-1] + ' says.')
            print('\'I am Arco. Arco of Kelp Ridge.\'')
            addFish(fishArray, arco)
            gotArco = True
    else:
        print('The fish\'s eyes widen when he sees Pizzicato.')
        print('\'Arco!\' Pizzicato shouts. ')
        print('The fish (presumably Arco) drops his knife. \'...Pizzicato?\'')
        print('\'Yes! Arco, it\'s me!\'')
        print('Arco turns to you. \'I think I will join you... for Pizzicato.\'')
        arco = personAttributes('Arco', 'the Fish', 13, 16, 17, 18, 14, 'Male', 'light gray', 'dark gray', 'ice blue',
                                None, None)
        addFish(fishArray, arco)
        gotArco = True
    return gotArco


def meetIodine(Team, items, metIodine):
    print('You and your team head toward the plain.')
    print('There is a green bush.')
    print('You know what happened last time, but still you head on.')
    print('Suddenly, you see a gray-white fish with vermillion fins.')
    print('In her fin is a intricate sea glass knife.')
    print('\'Hey! Who are you?\' you ask.')
    print('The fish\'s sea-blue eyes pierce into your soul.')
    print('\'My name is Iodine. Who are you?\'')
    input('Press enter to continue. ')
    print('You tell her your team\'s names, reluctantly.')
    if 'Kale the Fish' in Team:
        print('Iodine\'s eyes widen. \'..Kale?\'')
        print('Kale looks from Iodine to you then to Iodine.')
        print('Then, Kale leaps towards Iodine and traps her in a fish hug.')
        print('\'Kale...I thought you\'d died.\'')
        print('Kale takes Iodine\'s fin. \'But I survived.\'')
        print('Iodine does not pull away, but instead hugs Kale harder. \n \'This is for you, for helping me love again.\'')
        print('She leaves you a small crystal sphere, and with a final longing glance at Kale, she leaves.')
        items['Iodine\'s Sphere'] = ['orb', 'intelligence', 16]
        metIodine = True
    else:
        print('Iodine points her knife at your heart.')
        print('\'Okay...tell me where your master Dab is.\'')
        print('You say, \'I don\'t know. He\'s not my master.\'')
        print('\'Then who are you working for?\'')
        print('A smile curls your lips. \'I am the leader of my fish.\'')
        print('Iodine sighs. \'So then where is he!\'')
        print('You shrug. \'I seriously don\'t know!\'')
        print('\'Then leave. This is my place, and I can kill you if I want.\'')
        metIodine = True
    return metIodine, items


def meetPizzicato(Team, fishianGold, metPizz):
    print('You and your team head toward the plain.')
    print('There is a green bush.')
    print('Oh no! You see a fish skulking by.')
    print('You can attack or hide.')
    desicion = input('But which one?(a/h) ')
    if desicion == 'a':
        if 'Arco the Fish' in Team:
            print('The fish\'s eyes widen. \'Arco?\'')
            print('\'Pizzicato!\' Arco says.')
            print('\'I  will join you... for Arco.\' the fish(presumably Pizzicato) says.')
            pizzicato = personAttributes('Pizzicato', 'the Fish', 8, 18, 15, 17, 6, 'Female', 'jet black', 'light gray',
                                         'grass green', None, None)
            addFish(fishArray, pizzicato)
            fishianGold += 250
        else:
            losses = 0
            print('Attack! If a fish has over 12 strength and over 14 intelligence, they may win.')
            for i in Team:
                if (fishArray[i].strength > 12) and (fishArray[i].strength > 14):
                    print(i + ' has beaten the fish!')
                    break
                else:
                    print(i + ' was unable to defeat the fish.')
                    losses += 1
            if losses == len(Team):
                print('The fish has defeated all. She robs you of your Fishian gold and leaves.')
                fishianGold = 0
                print('\'I am Pizzicato! And I am your death.\'')
            else:
                print('The fish,  battered and wet with her own blood, leaves.')
                if fishArray[i].strength > 19:
                    print('\'What--I\'ve never met so strong a fish.\'')
                    print('\'Maybe I\'ll join you...\'')
                    pizzicato = personAttributes('Pizzicato', 'the Fish', 8, 18, 15, 17, 6, 'Female', 'jet black',
                                                 'light gray', 'grass green', None, None)
                    addFish(fishArray, pizzicato)
                    fishianGold += 250
                else:
                    print('\'Don\'t come back.\'')
        metPizz = True
    elif desicion == 'h':
        print('Sadly the one green bush is insufficient for hiding.')
        if 'Arco the Fish' in Team:
            print('The fish finds you...but then')
            print('the fish\'s eyes widen. \'Arco?\'')
            print('\'Pizzicato!\' Arco says.')
            print('\'I  will join you... for Arco.\' the fish(presumably Pizzicato) says.')
            pizzicato = personAttributes('Pizzicato', 'the Fish', 8, 18, 15, 17, 6, 'Female', 'jet black', 'light gray',
                                         'grass green', None, None)
            addFish(fishArray, pizzicato)
            fishianGold += 250
        else:
            print('The fish quickly finds you and robs you of your Fishian gold.')
            fishianGold = 0
            print('\'I am Pizzicato! And I am your death.\'')
        metPizz = True
    return fishianGold, metPizz


def yourKingdomAdventure(Team, gotGold, gotArco, metPizz, fishianGold, metIodine, items):
    print('Your kingdom? Seriously?')
    input('Press enter to continue.')
    print('You decide to go either to the forest or plain.')
    decision = input('But which one? (f/p)')
    if decision == 'f':
        print('You and your team go towards the forest.')
        print('In here there is bushy undergrowth, almost like a maze.')
        neededInt = random.randint(4, 12)
        print('A fish must have at least ' + str(neededInt) + ' intelligence to pass.')
        for i in Team:
            if fishArray[i].intelligence >= neededInt:
                print(i + ' has made it out!')
            else:
                print(i + ' could not make it and turned back.')
                Team.remove(i)
        if gotGold == False:
            print('Your team comes out into a grassy clearing and finds a small sack!')
            print('Oh my fish! It\'s 15 Fishian gold!')
            fishianGold += 15
            gotGold = True
        elif gotArco == False:
            gotArco = meetArco(Team, gotArco)
        else:
            print('Your team comes out in a grassy clearing.')
            print('There is nothing here.')
    elif decision == 'p':
        if metPizz == False:
            fishianGold, metPizz = meetPizzicato(Team, fishianGold, metPizz)
        elif metIodine == False:
            metIodine, items = meetIodine(Team, items, metIodine)
        else:
            print('You and your team head toward the plain.')
            print('There is a green bush, but nothing else.')

    return gotGold, gotArco, metPizz, fishianGold, metIodine, items


def cloudMountainAdventure(Team, borderCrossed, guardsDefeated, gotMoreGold, metEndurance, gotOrb, gotYay, fishianGold, fishFood):
    print(
        'Ahh. The snowy breeze blows past you at the foot of the mountains, \n and above you there are beautiful snow-studded peaks.')
    input('Press enter to continue. ')
    print('You can stay at the foot of the mountains, head to the shortest peak, or head to the tallest.')
    decision = input('But which one? (f/s/t)')
    if decision == 'f':
        print('Frost covered brush lines the foot of the mountain range, and an icy pine forest stands to your left.')
        print('But suddenly you realize: There\'s a fish, high in the mountaintops, watching you!')
        print('Their orange scales stand out against the pure-white peaks.')
        print('It\'s just a fish, you assure yourself. It won\'t harm you.')
        desicion = input('Do you explore the brush or the pines? (b/p) ')
        if desicion == 'b':
            if borderCrossed == False:
                print('You and your team explore the brush lining the foot of the mountains.')
                print(
                    'A flash of metal catches your eye. It\'s a wickedly jagged knife, \n tied delicately to the brush to point directly at your head.')
                print(
                    'You back away, but it\'s too late. The brush behind you has closed in a cage shape, and you are trapped.')
                print('A twilight fish with sky blue fins and mint-colored eyes assaults you from the front,')
                koyden = personAttributes('Köyden', 'Kyda', 16, 36, 19, 12, 14, 'Female', 'twilight', 'sky blue',
                                          'mint green', None, None)
                # Köyden only joins your team at the very, very end, if she ever does.
                # Lore: Köyden was the one to injure/almost kill Arco and Kale. She also killed many a good fish.
                # She is also one of Dab's best generals. But loyalty? Maybe not...she has plans for killing Dab and taking over Fishland. Hehe!
                print('followed by two other fish, both vermillion with orange yellow fins.')
                print('Weirdly, their eyes are stormy purple, without a trace of pupil.')
                print('\'Hey! You! You\'ve trespassed on our territory.\' the twilight fish yells.')
                print('\'Your territory?\' you reply dubiously.')
                print('\'Not mine. Dab\'s.\' she says.')
                print('You notice a dark opening behind the three fish. A cave, with a fish trapped inside. ')
                print(
                    '\'Go now.\' she threatens. \'Go now, or I\'ll have to kill you. And believe me, I don\'t want to.\'')
                print('\'Of course not.\' you reply. \'This is MY kingdom! You cannot threaten me here.\'')
                print('The fish\'s lips curl into a dark smile. \'I\'m sorry. But you have to die.\'')
                print('In one fluid movement, she grabs the knife from the brush and points it at your eye.')
                print("'You know too much. And now... ")
                input(' ')
                print('you will die!\'')
                print('She stabs the knife downward, but you evade the attack, throwing her off balance.')
                print('You grab it from her grasp and press her down onto the ground.')
                print('\'You will regret this!\' she screams as she wriggles free and runs away. \'I will tell Dab!\'')
                print('A fish walks out of the cave, soft gray-white with light gray fins and forest green eyes.')
                print('\'I am Silicon. And I take that you are here to rescue me.\'')
                borderCrossed = True
                input('Press enter to continue.')
                print('The twilight fish comes racing back, with ten or so purple-eyed fish following.')
                print('\'Go. Go or die.\'')
                print('You reluctantly leave, casting one last glance at Silicon.')
                print(' ')
                print('A smile slowly tugs at the corners of your mouth.')
                print('After all, you still have the twilight fish\'s knife.')
                items['Köyden\'s Knife'] = ['weapon', 'knife', 6]
            elif guardsDefeated == False:
                print('You and your team explore the brush lining the foot of the mountains.')
                print('As expected, the twilight fish is back, but with no other fish with her.')
                print('\'You again!\' she yells.')
                print('\'Yes, it\'s me.\' you reply calmly.')
                print('Her fins grasp the hilt of her weapon. \'Well, if I were you, I would run.\'')
                print('You smile. \'But you\'re not me. And I WILL FIGHT!\'')
                print('\'Ah!\' she exclaims. \'But defeating me is not so easy.\'')
                print('\'Wait, who ARE you?\' you question.')
                print('\'My name...is Köyden. And I am your doom.\'')
                print('A flurry of raging strikes hits your team. They must have at least 17 agility to dodge.')
                losses = 0
                for i in Team:
                    if fishArray[i].agility >= 17:
                        print(i + ' was successful in dodging the attack.')
                    else:
                        print(i + ' could not dodge the attack and fell back, wounded.')
                        losses += 1
                if losses >= 1:
                    print('\'Ha, you see?\' she smirks. \'Your team will fall when it is time.\'')
                print('She lowers her twin knives. ')
                print('\'Leave.\' she threatens. \'Leave, or I will kill you.\'')
                desision = input('Do you attack or leave? (a/l)')
                if desision == 'a':
                    print('You leap towards Köyden, trying to throw her off balance.')
                    print('It doesn\'t work and she stabs you.')
                    if (fishArray[Team[0]].strength >= 19) and (fishArray[Team[0]].intelligence >= 19) and (
                            fishArray[Team[0]].agility >= 19):
                        print('But you are strong and smart and fast, so you use a fish-karate chop to her face.')
                        print('Köyden falls back, injured. Then she stabs you again.')
                        print('Then you heave a PUNCH to her STOMACH!')
                        print('She falls unconscious to the cave floor.')
                        print('You grab her knives. They are now yours.')
                        items['Köyden\'s Twin Knives'] = ['weapon', 'knife', 19]
                        guardsDefeated = True
                        input(' ')
                        print('Silicon steps out of the cave.')
                        print('\'Thank you...for saving me.\'')
                        silicon = personAttributes('Silicon', 'the Fish', 17, 13, 32, 14, 18, 'Female',
                                                   'soft gray-white', 'light gray', 'forest green')
                        addFish(fishArray, silicon)
                    else:
                        print('You are injured and leave.')
                elif desision == 'l':
                    print('You leave, looking back at the fish who has killed and the fish who is imprisoned.')
            else:
                print('You and your team explore the brush lining the foot of the mountain.')
                print('There is a cave with creepy archaic script all over the walls.')
                print('But other than that, there is nothing here.')
                read = input('Do you want to read the text? (y/n)')
                if read == 'y':
                    scripts = [
                        'A fish will come to save the land.',
                        'There will be a fish one day who will doom Fishland if not stopped.',
                        'Fishes can be good and brave but they can also be evil.',
                        'Two fish once together will reunite.'
                    ]
                    print('It is hard to read, but you see something: ')
                    print(random.choice(scripts))
        elif desicion == 'p':
            if gotMoreGold == False:
                print('You and your team explore the pines to your left.')
                print('Twisted and broken shards of sea glass and Fishian iron line the snowy ground, ')
                print('and one lone sword lays embedded in the ice.')
                print('Was there a battle here?')
                print('Ah! You see the familiar glint of Fishian gold.')
                print('It\'s 75 Fishian gold! You quickly store it in a pouch.')
                print('But then you see the orange fish again, and decide to leave.')
                gotMoreGold = True
            else:
                print('You and your team explore the pines to your left.')
                print('Twisted and broken shards of sea glass and Fishian iron line the snowy ground,')
                print('and one lone sword lays embedded in the ice.')
                print('But other than that, there is nothing.')
    elif decision == 's':
        print('Your team heads toward the shortest peak.')
        print('Oh no! It\'s a snowstorm!')
        decicion = input('Do you take shelter or keep going? (t/k) ')
        if decicion == 't':
            if metEndurance == False:
                print('You and your team take shelter behind some rocks.')
                print('Ah! There\'s a fish hiding with you!')
                print('\'Who are you?\' you ask.')
                print('The fish, surprised at being found, does not speak.')
                print('\'I said, who are you?\' you question.')
                print('The fish fidgets with a small pouch. \'My name is Endurance.\'')
                print('You see that he is dark brown with white fins and sunrise colored eyes.')
                print('The snowstorm passes. Endurance asks, \'Who are you with, Dab or Shif?\'')
                print('\'Who is Shif?\' you ask.')
                if 'Fidget the Fish' in Team:
                    print('Fidget looks very surprised.')
                print('Endurance facepalms(facefin?). \'You don\'t know Shif?\'')
                print('\'No, who is Shif?\' you question. ')
                print('\'Shif, the one fish who dare stand against Dab.\' he replies calmly.')
                print('\'I know Dab, and he isn\'t my friend.\' you say. \'But WHO the FISH is SHIF?\'')
                print('\'Then are you with Shif?\' he asks.')
                print('You explode. \'How am I supposed to know if I\'m with Shif if I don\'t even know her?\'')
                print('Endurance shrinks away. \'Bye?\'')
                print('Your team watches as the young fish treks off into the mountains.')
                print('Another snowstorm hits, stronger than ever. You decide to leave.')
                metEndurance = True
            else:
                print('You and your team take shelter behind some rocks.')
                print('This time, Endurance is not here with you.')
                print('The snowstorm rages higher, harder, and you decide to leave.')
        elif decicion == 'k':
            if gotOrb == False:
                print('You keep going despite the storm.')
                if 'Arco the Fish' in Team:
                    print('\'Look! It\'s a fish!\' Arco exclaims.')
                else:
                    print('You notice there\'s a fish on the mountainside.')
                print('But as soon as you spot them, though, they\'re gone.')
                print('The snowstorm stops. You find a fish on the mountaintop.')
                if metEndurance == True:
                    print('Ah! It\'s Endurance!')
                else:
                    print('\'What is your name?\' you ask.')
                    print('\'My name is Endurance\', he replies.')
                print('The sky is getting dark, you realize.')
                print('Endurance leaves, trotting down the mountain.')
                print('You decide to stay for a while when you see a rolled up note on the snow.')
                print('    \'' + Team[0] + ''',
    Nowadays even the young fish know that
    there are not many fish one can trust.
    But I hope
    that one of those fish is me.
        -Endurance the Fish''' + '\'')
                print('You find a small crystal orb by the note.')
                print(Team[1] + ' marvels at it. \'It\'s a pure globe of agility!\'')
                print('You pick it up, and leave.')
                items['Endurance\'s Orb'] = ['orb', 'agility', 5]
            else:
                print('You see Endurance sitting on the mountaintop, gazing at the sky.')
                print('\'Hey! Do you want to trade Fishian gold and Fish Food? \'')
                dessiion = input('Do you? (y/n) ')
                if dessiion == 'y':
                    offer = input('\'Well then which one do you want to trade? (g/f) \'')
                    offerNum = input('\'Then how much?\'')
                    try:
                        offerNum = int(offerNum)
                    except ValueError as error:
                        print('That isn\'t a number.')
                        offerNum = 0
                    if offer == 'g':
                        if offerNum > fishianGold:
                            print(
                                '\'I\'ve seen through your trickery, fish! You say you have more than you really do.\'')
                        else:
                            returnNum = offerNum // 2
                            print('Endurance hands you ' + str(returnNum) + ' Fish Food.')
                            fishFood += returnNum
                    if offer == 'f':
                        if offerNum > fishFood:
                            print(
                                '\'I\'ve seen through your trickery, fish! You say you have more than you really do.\'')
                        else:
                            returnNum = offerNum * 2
                            print('Endurance hands you ' + str(returnNum) + ' Fishian gold.')
                            fishianGold += returnNum
    elif decision == 't':
        print('You and your team trod towards the highest peak.')
        print('The snow is freezing, cutting at your fins and numbing them.')
        print('Then, you see the familiar glint of orange. Carrots!')
        print('Pulling yourself up, you see that the carrots are still fresh.')
        print('But it may as well be a trap.')
        pick = input('Do you pick them? (y/n) ')
        if pick == 'y':
            if gotYay == False:
                print('You and your team tug hard at the carrots, ')
                print(' but then you feel something truly fishy: scales!')
                print('You pull, and...')
                input(" ")
                print('BOOM! It\'s a fish for sure. The fish who\'s been stalking you!')
                print('\'Who are you?\' you screech.')
                print('The fish looks from you to the carrots then back to you.')
                print('\'Go away!\' he yells. \'Go away if you don\'t want to die!\'')
                print('\'Ha.\' ' + Team[1] + ' says. \'You don\'t even have any weapons!\'')
                print('The fish looks fearful for some reason.')
                print('\'So you won\'t go? Then die.\'')
                yay = personAttributes('Yay', 'the Fish', 6, 19, 4, 16, 34, 'Male', 'bright orange', 'grass green', 'mint green', None, None)
                for i in Team:
                    print(i+' steps up. \'I don\'t know about you, but I know I will win.\'')
                    yayStratagems = createStratagemList(1000, ['Sweep', 'Ambush', 'Raise the Dead'])
                    yayStratagems[0] = 'Un-Mutate'
                    breakForUnMutation, loser = battle(fishArray[i], 200, 200, yay, 500, 1000, yayStratagems)
                    if loser == 'the fish':
                        break
                if loser == 'the fish':
                    print('The fish gapes at you.')
                    print('\'So you\'re not with Dab?\'')
                    print('\'Yeah.\' you reply.')
                    print('\'I\'m Yay. Mind if I join you?\'')
                    gotYay = True
                    addFish(fishArray, yay)
            else:
                print('You pick the carrots and eat, relishing their taste.')
                print('In these times, food is scarce, but here there is so so much!!')
                fishFood += random.randint(5, 100)
        elif pick == 'n':
            print('You don\'t pick the carrots.')

    return borderCrossed, guardsDefeated, gotMoreGold, metEndurance, gotOrb, gotYay, fishianGold, fishFood


def mineralValleyAdventure(ded, Team, metShale, valorAsked, andesiteRAWR, fishianGold, fishFood):
    print('Your team treks through the rocky valley to arrive at a crossroads.')
    print('A rock mine stands to your left, and a towering shale palace soars into the clouds.')
    print('Then you notice a small wood. A fish peeps out.')
    decision = input('Do you go to the mine, the palace, or the wood? (m/p/w) ')
    if decision == 'm':
        print('The mine has jagged, rocky walls. Two soot-stained fish are digging.')
        approaching = input('Do you approach the fish? (y/n) ')
        if approaching == 'y':
            if metShale == False:
                print('\'Hi!\' you call out. The younger of the two fish looks at you weirdly.')
                print('The other fish calls out. \'Hey! I\'m Lime and she\'s Shale.\'')
                print('Shale glares at you and resumes poking around with her pickaxe.')
                print('\'What\'s your name?\' Lime asks inquisitively.')
                print('\'My name is '+Team[0]+'.\' you reply.')
                print('\'Nice to meet you.\' he winks.')
                print('Shale pokes Lime with her pickaxe. \'Shut up!\'')
                print('\'If we could talk in PRIVATE?\' Shale asks.')
                print('You back away politely. \'Oh of course!\'')
                print('The two fish jabber away. You can hear some shreds of conversation.')
                print('\'Conspiracy\'...\'Dab\'...\'Can\'t trust them\'...')
                print('You decide to leave.')
                metShale = True
            elif 'Find Lime' not in completedMissions:
                print('\'Hi!\' you call out to the fish you know are named Lime and Shale.')
                print('\'Hi..?\' Shale replies.')
                print('You edge closer. \'How is the mining going?\'')
                print('\'Horrible,\' Shale says. \'Go away.\'')
                print('\'Where\'s Lime?\' you question.')
                print('\'Lime ran off.\' she replies sadly. \'If you could find him...\'')
                print('\'Oh yes I can!\' you say.')
                print('Shale\'s eyes go wide. \'You can find him?\'')
                print('\'I can!\'')
                if 'Find Lime' not in missionArray:
                    missionArray['Find Lime'] = 'Find Lime, a fish who ran away. Reward: 1 piece of shale ore'
            else:
                print('\'Hi!\' you call out to the fish you know are named Lime and Shale.')
                print('\'Hi..?\' Shale replies.')
                print('\'How\'s it going?\' you ask.')
                print('\'Boring.\' Shale says. \'Now go away.\'')
                print('You leave.')
        else:
            print('You decide against approaching the fish.')
            print('You catch the younger one watching you, then whispering to the other.')
            print('Feeling weird, you decide to leave.')
    elif decision == 'p':
        print('You see the palace gates are thrown wide open.')
        if andesiteRAWR == False:
            print('A carmine fish is sitting on the throne, with another smaller jet black fish beside.')
            print('With a flick of his fin, the carmine fish welcomes you in.')
        input('')
        if valorAsked == False:
            print('You approach the fish with caution.')
            print('\'Welcome to Mineral Valley!\' the carmine fish exclaims.')
            print('The jet-black fish slaps the carmine one. \'Don\'t mind Valor. The leader thing is getting into his head.\'')
            print('\'Valor?\' you echo.')
            print('\'Yes, he\'s Valor.\' the jet-black fish sniffs. \'He\'s overrated.\'')
            print('Upon looking at the jet-black fish, you are filled with a strong sense of déjà vu.')
            print('Have you seen her before?')
            print('You cock your head. \'What is your name, then?\'')
            print('\'My name is Andesite.\' she responds. \'What are you here for?\'')
            print('\'Nothing really.\' you say.')
            print('Andesite points a fin at Valor. \'Then he\'ll be able to help you.\'')
            print('She promptly exits the room.')
            print('\'Has your kingdom been taken by Dab?\' you ask Valor.')
            print('\'Ah...\' Valor slurs. \'Maybe.\'')
            print('Hopefully, you think, this Maybe means no.')
            valorAsked = True
        elif andesiteRAWR == False:
            print('You approach, knowing they are Valor and Andesite.')
            print('You see that they are both very tense. \'We\'ve heard Dab\'s coming.\' Valor says.')
            print('\'Dab?\' you jolt up. \'He\'s coming?\'')
            print('\'Sadly yes.\' Andesite responds. \'Dab\'s spy is in the camp.\'')
            findSpy = input('Do you wish to help the fish find the spy? (y/n) ')
            if findSpy == 'y':
                print('These are possible spies in the camp')
                if 'Talc the Fish' in Team:
                    possSpies = ['Andesite', 'Valor', 'Lime', 'Shale', 'Evda']
                else:
                    possSpies = ['Andesite', 'Valor', 'Lime', 'Shale', 'Talc', 'Evda']
                print(possSpies)
                if 'Pizzicato the Fish' in Team:
                    print('Pizzicato points at Evda\'s name. \'Hey! I know Evda. She\'s not to be trusted.\'')
                if metShale == True:
                    print('\'Shale looks suspicious.\' '+Team[1]+' says.')
                if 'Fidget the Fish' in Team:
                    print('Fidget looks excited to solve the mystery. \'I think we can\'t trust Valor.\'')
                if 'Talc the Fish' in Team:
                    print('\'Don\'t trust Lime or Shale!\' Talc exclaims.')
                if 'Silicon the Fish' in Team:
                    print('Silicon shrugs. \'It could be Valor or Andesite, but I think the spy is Shale.\'')
                if '\'The Boys\' the Fish' in Team:
                    print('\'It has to be Lime. I know it.\' \'The Boys\' murmurs.')
                if 'Talc' not in possSpies and 'Kale the Fish' in Team:
                    print('Kale paws the ground with her fins. \'It\'s Talc, I know it\'s Talc.\'')
                possSpy = ''
                while possSpy not in possSpies:
                    possSpy = input('Who do you think the spy is?')
                if possSpy == 'Andesite':
                    print('\'Me?\' Andesite asks.')
                    print('\'Yes. It\'s you.\' you say.')
                    print('She draws a sharp blade from her sheath.')
                    print('With a swift motion, she stabs Valor. \'Yes, it\'s me.\'')
                    print('\'But will you live to tell it?\'')
                    print('She leaps at you, and suddenly you are locked in combat.')
                    andesite = personAttributes('Andesite', 'Kelp', 17, 28, 38, 9, 13, 'Female', 'jet black', 'jet black', 'vermillion')
                    breakForUnMutation, loser = battle(fishArray[Team[0]], 200, 200, andesite, 300, 1800, normalEnemyStratagems)
                    if loser == 'you':
                        print('Andesite plants a fin on your body. \'You lost.\'')
                        print('\'Ummghh.\' you say through her fin.')
                        print('\'Since I\'m in a good mood, I\'ll let you go.\'')
                        print('\'But mention ONE word of this to Köyden, and she\'ll kill me.\'')
                        print('\'Now GO!\'')
                        print('You run across the palace floor, across the grass, across the snowy plain.')
                        print('You have a feeling you won\'t be coming here anytime soon.')
                        andesiteRAWR = True
                    else:
                        print('Andesite crumples onto the ground, and you poke her.')
                        print('\'Go away.\' she sobs. \'Stop.\'')
                        reassuring = input('Do you decide to reassure her? (y/n) ')
                        if reassuring == 'y':
                            print('\'It\'s okay.\' you say. \'Any fish can change.\'')
                            print('She kicks you with her tail. \'I\'m a evil fish, and no one can change that.\'')
                            print('You hold out a fin. \'You can join us.\'')
                            print('She gets up, tucking her blade into her sheath.')
                            if random.randint(0, 2) == 0:
                                print('But then her weapon flashes, and everything goes black.')
                                print('\'You\'re too trusting. Now, goodbye.\'')
                                ded = True
                            else:
                                print('Looking back at her homeland, Andesite smiles softly.')
                                print('\'Watch out, Mineral Valley. I\'ll be back.\'')
                                addFish(fishArray, andesite)
                        else:
                            print('You leave.')
                        andesiteRAWR = True
                else:
                    print('No fish responds, all asleep.')
                    print('You probably took too long thinking!')
            else:
                print('You go away, thinking of who the spy may be.')
        else:
            if 'Andesite Kelp' in fishArray.keys():
                print('The palace still has its former glory, but a new leader sits on the throne.')
                print('Andesite gasps. \'Evda.\'')
            else:
                print('The palace is deserted. A small jet-black fish lingers at the side.')
    elif desicion == 'w':
        print('You make your way to the wood.')
        print('Tangled vines poke out from the dark brush.')
        stat = random.randint(9, 19)
        print('A fish must have at least '+str(stat)+' instinct to pass safely.')
        for i in Team:
            if fishArray[i].instinct >= stat:
                print(i+' has made it out safely.')
            else:
                print(i+' could not make it and returned to the camp.')
                Team.remove(i)
        if len(Team) > 0:
            if 'Talc the Fish' not in fishArray.keys():
                print('You come out in a small clearing where there is a small hut.')
                print('A small fish peeks out.')
                print('\'Hi! I\'m Talc!\' he says. \'If you beat me in a duel, I will join you.\'')
                talc = personAttributes('Talc', 'the Fish', 15, 9, 12, 16, 7, 'Male', 'coral pink', 'neon pink', 'forest green', None, None)
                duel = input('Do you accept? (y/n) ')
                if duel == 'y':
                    print('Talc steps up.')
            
                    breakForUnMutation, loser = battle(fishArray[Team[0]], 200, 200, talc, 200, 400, normalEnemyStratagems)
                    if loser == 'the fish':
                        print('\'Fine, you won.\' Talc says. \'I\'ll join you.\'')
                        addFish(fishArray, talc)
                    else:
                        print('\'You...couldn\'t even defeat a lowly fish like me...what the heck..\'')
                else:
                    print('You decline the offer. Talc goes away.')
            elif metAkuma == False:
                print('You come out in a small clearing.')
                print('Suddenly a fish jumps out, holding a katana.')
                print('\'Hey! Who are you?\' she asks.')
                print('\'I\'m '+Team[0]+'.\' you reply.')
                print('She tosses her katana into the air. \'Haven\'t met you.\'')
                print('\'Me neither.\' you reply as the fish catches her katana with a flourish.')
                print('\'Wait, who are you?\' you ask.')
                print('The fish again twirls her katana. \'My name?\'')
                print('\'Your name.\'')
                print('\'Well, I\'m Akuma. I don\'t have any friends, but if I did...')
                print('..they\'d call me Aku for short.\'')
                print('You furrow your brow. \'Akuma what?\'')
                print('Akuma rolls her eyes. \'Kelp. Now shut the eff up or I\'ll kill you.\'')
                print('\'Okay, then will you join us?\' you ask.')
                print('\'You? You puny fish? Hell no.\' Akuma sheaths her katana.')
                print('\'And being a devil, I have quite the experience with hell.\'')
                keep = input('Do you keep pushing Akuma to join you? (y/n) ')
                if keep == 'y':
                    print('\'Okay, great.\' you say.')
                    print('Akuma glares. \'That was your cue to go away.\'')
                    print('You glare back. \'No, it was not.\'')
                    print('\'Was that a glare?\' she asks cooly.')
                    print('\'Yes, it was.\' you answer.')
                    print('\'No fish dares glare at me, kelp-brain.\' she slowly draws her katana.')
                    print('You explode. \'WELL JUST COME ON! COULD YOU JOIN US?? WE COULD DEFEAT DAB! KÖYDEN EVEN!\'')
                    print('Akuma cocks her head. \'Köyden? Now that\'s a fish I\'d like to kill.\'')
                    print('\'But nooo.\' she continues. \'Not with you.\'')
                    print('Your hopes shattered, you leave.')
                else:
                    print('You leave.')
                metAkuma = True
            elif 'Akuma \'Aku\' Kelp' not in fishArray.keys():
                print('You come out in a small clearing.')
                print('Akuma is standing in the center, katana flying as she demolishes a wall of thick brush.')
                print('She spots you, and glares in your direction.')
                fight = input('Do you challenge her to a fight? ')
                fight = fight + 'placeholder'
                if fight[0] == 'y':
                    print('You edge closer. \'Akuma!\'')
                    print('She swings her katana in your direction. \'what.\'')
                    print('\'I\'ll challenge you to a duel.\'')
                    print('\'Huh.\' Akuma murmurs. \'If you lose, I get to kill you.\'')
                    print('\'And if I win...\' you say. \'Then you have to join me.\'')
                    print('\'Fine.\' Akuma says. \'Bring it on.\'')
                    akuma = personAttributes('Akuma \'Aku\'', 'Kelp', 22, 34, 17, 12, 7, "Female", "aku indigo", 'aku blue', 'aku blue')
                    for i in Team:
                        breakForUnMutation, loser = battle(fishArray[i], 200, 200, akuma, 1260, 1728000, normalEnemyStratagems)
                        if loser == 'the fish':
                            print('\'Fine.\' Akuma sulks. \'You won.\'')
                            break
                    if loser == 'the fish':
                        print('\'I\'ll join your team...\'')
                        addFish(fishArray, akuma)
                    else:
                        print('\'Ha! I told you you were no match for me...\'')
            else:
                print('You come out in a small clearing.')
                print('An unused sheath lies on the ground.')
                print('But other than that, there is nothing.')
                
    return ded, metShale, valorAsked, andesiteRAWR, fishianGold, fishFood


def peakDepthsAdventure(ded, Team, items, fishianGold, gotIrn, metCinnabar):
    print('Your team makes their way to Peak Depths.')
    print('Deep ravines stretch deep into the rocky ground, ')
    print('and towering peaks climb into the clouds.')
    decision = input('Do you go into the ravine or up towards the peak? (r/p) ')
    if decision == 'r':
        print('You climb down into the ravine.')
        if metCinnabar == False:
            if 'Akuma the Fish' not in Team:
                print('A fish jumps out at you. \'HA! Found you, Aku..whaa?\'')
                print('\'I\'m not whoever you think I am.\' you reply.')
                print('\'Oh dang it.\' says the fish. \'Anyways! Give me all your Fishian gold!\'')
                if 'Pizzicato the Fish' in Team:
                    print('Pizzicato rolls her eyes. \'You\'re doing it all wrong.\'')
                    print('\'What?\' the fish asks.')
                    print('\'Well first--\' Pizzicato stops abruptly. \'What is your name?\'')
                    print('\'Cinnabar... Cinnabar Kelp.\'')
                    print('\'Cinnabar?\' Pizzicato asks. \'Cinnabar?\'')
                    print('Cinnabar looks uncomfortable. \'Yeah..\'')
                    print('Pizzicato gazes in the direction of Kelp Ridge. \'I know you.\'')
                    print('Pizzicato continues: \'You were there, when Dab and Köyden took over Coral Shallows.\'')
                    print('\'You were there, in the midst of the turmoil, collecting coral. What was it?\'')
                    print('Cinnabar smiles.\'It was the only bit of Kydian Coral left.\'')
                    print('\'Kydian Coral?\'')
                    print('\'It\'s one of the components of the immortality formula.\'')
                    print('Cinnabar looks peaceful. \'And now I finally have a fish to give it to.\'')
                    print('She holds out her fin, and from it Pizzicato takes a tiny slab of coral.')
                    print('\'Hey--I forgot to ask!\' Cinnabar says. \'Who are you?\'')
                    print('Pizzicato looks sad. \'Pizzicato of Kelp Ridge.\'')
                    items['Kydian Coral'] = ['ingredient', 'coral', 'kydian']
                else:
                    print('\'Uh..no.\' you say. And with a flourish of your knife, the fish is bleeding, ')
                    print('but the wound is not deep enough to kill her.')
                    print('Looking at you in fear, the fish retreats into the ravine.')
            else:
                print('A fish jumps out at you. \'HA! Found you, Aku...wait, is it you?\'')
                print('Akuma\'s eyes instantly light up. \'..Cinnabar...Cinna?\'')
                print('\'Aku!\' the fish, presumably Cinnabar, yells happily.')
                print('Then the two fish turn and look at you. \'Uh...\'')
                print('\'It\'s okay, you can leave.\' you reluctantly say.')
                print('\'You sure...?\' asks Cinnabar.')
                print('\'Yeah...\' you say, looking away. \'Go. Go before I change my mind.\'')
                print('Akuma and Cinnabar head off into the distance. Akuma waves.')
                del fishArray['Akuma \'Aku\' Kelp']
                metCinnabar = True
        elif gotIrn == False:
            print('Ah! You see the glint of Fishian iron.')
            print('It is a great hard slab and you pick it up happily.')
            print('A fish comes running towards you!!!')
            print('He is crimson with vermillion fins')
            print('and sparkling gray-white eyes.')
            print('\'Hey\' he says. \'Are you lost?\'')
            print('\'Nah.\' you reply. \'What\'s your name?\'')
            print('\'Arkai.\' the fish replies.')
            print('\'Oh, nice to meet you.\' you respond, scanning Arkai for any concealed weapons.')
            print('You grip the Fishian iron harder. \'Bye we have to go.\'')
            print('\'Bye!\' Arkai calls back.')
            try:
                items['Fishian Iron'][2] += 1
            except KeyError as error:
                items['Fishian Iron'] = ['material', 'fishian iron', 1]
            gotIrn = True
        else:
            print('You see a fish, it\'s Arkai.')
            mats = ['Fishian Iron', 'Wood', 'Stone', 'Mineral']
            mat = random.choice(mats)
            print('\'Hey!\' Arkai calls. \'Want to buy some '+mat+'?\'')
            print('\'Naw.\' you reply.')
            print('\'But the price of '+mat+' has never been so low~ \'')
            matnums = createStratagemList(100, [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7])
            matnum = random.choice(matnums)
            print('\'~ It\'s only 1 Fishian gold per '+matnum+' pieces!\'')
            buy = input('Do you buy '+mat+'? (y/n) ')
            if buy == 'y':
                gold = input('How much?')
                try:
                    gold = int(gold)
                except:
                    gold = len(gold)
                    print('\'What?\' Arkai asks. \'I\'ll take that as a '+gold+'\'')
                if gold > fishianGold:
                    print('You don\'t have that much!')
                else:
                    youget = gold * matnum
                    print('You get '+str(matnum)+' pieces of '+mat+'!')
                    fishianGold -= gold
                    items[mat][2] += matnum
    elif decision == 'p':
        print('You climb up towards the peak.')
        num = random.randint(15, 19)
        print('But, the winds are hella strong, and a fish must have '+str(num)+' strength to successfully pass.')
        for i in Team:
            if fishArray[i].strength >= num:
                print(i+' has made it up!')
            else:
                print(i+' could not make it and returned to camp.')
                Team.remove(i)
        if not len(Team) < 1:
            if 'Scalene the Fish' not in fishArray.keys() and 'Triangle Polygon' not in fishArray.keys():
                print('A crude dagger is embedded in the snowy underbrush.')
                print('And then you see: a fish has snuck up behind you!!')
                print('\'AIYAA!\' you bray, flipping around like a fish out of water. (fish?)')
                scalene = personAttributes("Scalene", "the Fish", 16, 24, 15, 29, 8, "Male", 'light gray', 'dark gray', 'hazel', perimeter, area)
                triangle = personAttributes("Triangle", "Polygon", 19, 12, 15, 1, 10, "Male", 'light gray', 'pale yellow', 'ice blue', isosceles, scalene)
                print('The fish is a light gray fish with dark gray fins and hazel eyes.')
                print('He is cradling another, smaller fish.')
                print('\'Who are you?\' you ask.')
                print('\'My name is Scalene. This is my son Triangle, and we need a home...\'')
                print('You take them back to your camp...')
                addFish(fishArray, scalene)
                addFish(fishArray, triangle)
            elif 'Triangle Polygon' not in Team and 'Scalene the Fish' not in Team:
                print('A crude dagger is embedded in the snowy underbrush.')
                print('Picking it up, you see a fish behind you.')
                print('He looks vaguely familiar, but you can\'t figure out who he is.')
                if random.randint(0, 1) == 1:
                    print('And then a gnarly branch slams into your head, and you blank out...')
                    input('Many hours later ')
                    print('You wake up in a dark cell. The fish is sitting beside you, chained.')
                    print('\'Who are you? Where are we?\' you ask, in a frenzy.')
                    print('The fish tries to say something, you can tell, but he doesn\'t.')
                    print('He points at the cell door, where a fish stands.')
                    print('As you are not chained, you get up off the floor, grab the crude dagger(why is it even there), ')
                    print('and leap at the guard, who is looking the other way.')
                    print('She deflects the dagger, but tosses it back to you.')
                    print('\'You could escape. I would let you, but it\'s too late.\' she murmurs.')
                    print('And when you see the HORRIBLE TYRANT DAB open the cell door, your chest twists.')
                    print('The last thing you see is a bloody excutioner\'s knife swinging towards you...')
                    ded = True
                else:
                    print('\'Who are you?\' you ask.')
                    print('He looks calm. \'Triangle was here. Where is he now?\'')
                    print('\'Triangle?\' you gasp.')
                    print('\'Triangle? Yeah.\' he replies.')
                    print('You squirm, thinking if you should tell him. \'Er...\'')
                    print('And then you remember where you\'d seen this fish before.')
                    print('In the battle of Coral Shallows...')
                    global radiusflashback
                    print(radiusflashback)
                    print('Dropping the dagger, you back away, going back to your camp.')
    return ded, items, fishianGold, gotIrn, metCinnabar

def blossomAdventure(Team, items, fishianGold):
    print('Blossom, a place where trees bloom year-round...')
    print('The soft path is lined with petals: rose, cherry, peach...')
    print('A rose-glass palace stands to the north, and a dark graveyard is to the west.')
    print('To the southwest, a collecting of small worker\'s huts lie.')
    decision = input('Where do you want to go? (p/g/h) ')
    if decision == 'p':
        print('Your team heads towards the palace, wary of incoming danger.')
        if metSkyfall == False:
            sadPeep = Team[len(Team) - 1]
            print('Suddenly, a fish assaults your team, pinning down '+sadPeep+'.')
            print('\'Gah!\' you shout, leaping onto the pile of fish.')
            print('The fish flips you over and leaps onto you. Now 2 fish are under him.')
            print('You wriggle away, then draw a dagger. \'Who are you?\' you yell.')
            print('The fish smiles darkly. \'Why would I tell you?\'')
            print('\'I am the leader of Peach Springs!\' you shout.')
            print('\'But this is not Peach Springs.\' he smirks. \'This is Blossom.\'')
            print('\'It\'s not like you\'re leader of Blossom.\' you say.')
            print('The fish grins. \'Oh, but I am. Skyfall Shade, King of Blossom.\'')
            if not sadPeep == 'Silicon the Fish':
                print('You sputter. \'You are not!\'')
                print('Skyfall\'s grin darkens. \'You want proof?\'')
                print('He pulls out a rose gold crown with sea glass swirls.')
                print('You gape. \'That cannot be legit.\'')
                print('Skyfall points at a small engraving on the back of the crown.')
                print('It reads: Forever this crown shall rest in Blossom.')
                print('\'That is not legit.\' you say.')
                print('\'It is.\' Skyfall replies, stuffing it back into a small bag.')
                print('\'So what are you doing with '+sadPeep+'?\' you ask.')
            else:
                print('Silicon wriggles. \'Skyfall... SHADE? Do you know where Eclipse is?\'')
                print('Skyfall\'s eyes go wide. \'Eclipse? He went missing a few years ago.\'')
                print('\'I\'m pretty sure there was another Shade. What was their name?\' Silicon asks.')
                print('\'I don\'t remember.\' Skyfall murmurs, distant. \'She was exiled when I was very young...\'')
                print('\'But.\' Silicon cuts in. \'Let me go.\'')
                print('\'No.\' Skyfall replies. His voice is now laced with a dark edge.')
                print('Then Skyfall turns to you.')
                print('\'If you give me your place as leader, I\'ll free this fish.\'')
                print('\'No!\' You stab the dagger at Skyfall, hoping you can wound him.')
            print('Skyfall dodges the attack. \'You looking for a fight? Bring it on.\'')
            skyfall = personAttributes('Skyfall', 'Shade', 8, 9, 17, 16, 8, "Male", "yellow green", "lime green", 'yellow orange', None, None)
            breakForUnMutation, loser = battle(fishArray[Team[0]], 200, 200, skyfall, 1050, 5040)
            if loser == 'the fish':
                print('\'Impossible.\' Skyfall huffs, gasping for breath.')
                print('\'Possible.\' you say, taking the crown. \'Very possible.\'')
                items['The Crown of Blossom'] = ['artifact', 'blossom', False]
            else:
                print('\'Leader of Peach Springs...\' Skyfall crows. \'Not so strong after all.\'')
                print('\'Shut up.\' you gasp. \'You have that really nice armor thing!\'')
                print('\'Bring your own next time.\' he says, knocking '+sadPeep+' out and going towards his palace.')
                print('You watch, filling with guilt, as the two fish disappear into the distance.')
                del fishArray[sadPeep]
            metSkyfall = True
        print('You reach the castle gates, one gate swinging back and forth, the other closed shut.')
        print('You enter from the open gate, only to see the two sides of the palace have been split apart by a tall glass wall.')
        print('A tiny gold gate shows you a portion of the other half.')
        print('You can see, the half you are in has ornate sculptures of a fish, ')
        print('and the ceiling is a mess of stone and iron.')
        print('The sculptures of the other half have been torn down, closing off the sky with a ')
        print('stone arch supporting a glass roof, but that is all you can see.')
        print('You approach the inner palace door, the one that leads to the throne room.')
        print('A fish is sitting on the throne. No, not Skyfall.')
        print('\'Who are you?\' the fish says. \'I am King Llafyks(laf-ficks).\'')
        print('\'I am '+Team[0]+'.\' you respond.')
        print('\'Do you know a fish named Skylon?\' King Llafyks questions.')
        print('\'No.\' you say. \'Why do you ask?\'')
        print('\'She is working with Dab to attack your kingdom.\' he replies.')
        print('\'Wait-- How do you know it\'s MY kingdom?\' you say.')
        print('\'Uh...er...ugh...\' the king stutters. \'Someone told me.\'')
        print('You cock your head. \'Who?\'')
        print('King Llafyks taps his fins against the armrest. \'They said their name was Taro.\'')
        print('\'Talo? Like the great Kydian queen of early Fishland?\' you ask.')
        print('King Llafyks facepalms(facefin?). \'Not Talo, TARO. Taro Fawn.\'')
        print('You know that the Fawn bloodline is from Kelp Ridge, the Carp clan.')
        print('So why has this fish wandered so far from his home?')
        print('\'Ah!\' the king says, looking at the rose-gold clock. \'Better go.\'')
        print('He hustles out of the throne room, and you decide to leave.')
    elif decision == 'g':
        print('Your team makes their way towards the graveyard, mindful of dangers.')
        print('As you walk closer you can see among the grayness, a single ivory headstone stands.')
        print('You walk towards, squinting to read the carved text.')
        print('\'Evol Shiar, Raih\'s Love\'')
        print('By it, a small sea-glass stone stands.')
        print('\'Yotta B., daughter of Orethguad Battoy\'')
        print('You then see a small headstone with a pendant wrapped around.')
        print('\'Raya Kyda: Forever in my heart -Trae Hymni, Rever of Adykayar\'')
        print('You feel grateful you are still alive.')
        print('Suddenly, a fish leaps at you, covered with black cloth so you can see nothing but her brilliant lime green eyes.')
        print('\'It was a mistake to come here, fish.\' she snarls.')
        print('\'For this is my territory, my domain.\'')
        print('Pulling out a dagger in midair, she lands perfectly, pivoting to face you. \'I am Mona Forieh, heir of Anom.\'')
        print('\'Who--\' you shout, only to have the dagger pressed to your head.')
        print('\'Try to talk again, and you die.\' Mona hisses.')
        print(Team[1]+' leaps on top of Mona, pressing her down. You wrest the dagger from her grip.')
        print('\'Thanks.\' you mutter to '+Team[1]+', then spin to face Mona.')
        print('Even though she is trapped, Mona sneers at you. \'I see your confidence. Leader, I assume?\'')
        print('You gape. \'How did you know?\'')
        print('\'I have my ways. Peach Springs, I presume?\'')
        print('Your mouth hangs open. \'How?\'')
        print('Just as Mona is about to reply, you cut in. \'Are you trying to buy time?\'')
        print('\'I am a loner. I have no allies.\'')
        print('A shadow sweeps the graveyard. Two fish leap in.')
        print('\'But we do.\' the larger one smirks.')
        print('Mona\'s eyes go wide. \'Emuserpi!-- Ah. Retsa B\'Ala Foeht of the Alabaster Ha, I presume?\'')
        print('\'Hello, Mona.\' the smaller one says.')
        print('\'Come on, Kabak Noemoc.\' Mona sighs.')
        print('Retsa B\'Ala turns to you. \'Do you know how long we\'ve waited?\'')
        print('\'For a legendary leader of the Peach.\' Kabak echoes.')
        print('\'\'')
    return items, fishianGold

def trueAdventure(fishianGold, fishFood, team, place, kingdomStuff, items, completedInvasions):
    ded = False
    Team = team
    yourKingdomStuff = kingdomStuff[0]
    cloudMountainStuff = kingdomStuff[1]
    mineralValleyStuff = kingdomStuff[2]
    peakDepthsStuff = kingdomStuff[3]
    print(cloudMountainStuff)
    gotGold = yourKingdomStuff[0]
    gotArco = yourKingdomStuff[1]
    metPizz = yourKingdomStuff[2]
    metIodine = yourKingdomStuff[3]
    gotMoreGold = cloudMountainStuff[0]
    borderCrossed = cloudMountainStuff[1]
    guardsDefeated = cloudMountainStuff[2]
    metEndurance = cloudMountainStuff[3]
    gotOrb = cloudMountainStuff[4]
    gotYay = cloudMountainStuff[5]
    metShale = mineralValleyStuff[0]
    valorAsked = mineralValleyStuff[1]
    andesiteRAWR = mineralValleyStuff[2]
    metCinnabar = peakDepthsStuff[0]
    gotIrn = peakDepthsStuff[1]
    print(borderCrossed)
    if place == 'Your Kingdom':
        gotGold, gotArco, metPizz, fishianGold, metIodine, items = yourKingdomAdventure(Team, gotGold, gotArco,
            metPizz, fishianGold, metIodine, items)
    elif place == 'Cloud Mountains':
        if 'Cloud Mountains: Invasion' in completedInvasions:
            # print('Ah! Dab\'s guards are here! Come back later...')
            borderCrossed, guardsDefeated, gotMoreGold, metEndurance, gotOrb, gotYay, fishianGold, fishFood = cloudMountainAdventure(
                Team, borderCrossed, guardsDefeated, gotMoreGold, metEndurance, gotOrb, gotYay, fishianGold, fishFood)    
        else:
            print('Dab\'s control is too strong! You can go here after completing \'Cloud Mountains: Invasion\'')
    elif place == 'Mineral Valley':
        if 'Mineral Valley: Invasion' in completedInvasions:
            ded, metShale, valorAsked, andesiteRAWR, fishianGold, fishFood = mineralValleyAdventure(ded, Team, metShale, valorAsked, andesiteRAWR, fishianGold, fishFood)
        else:
            print('Dab\'s control is too strong! You can go here after completing \'Mineral Valley: Invasion\'')
    elif place == 'Peak Depths':
        if 'Peak Depths: Invasion' in completedInvasions:
            ded, items, fishianGold, gotIrn, metCinnabar = peakDepthsAdventure(ded, Team, items, fishianGold, gotIrn, metCinnabar)
        else:
            print('Dab\'s control is too strong! You can go here after completing \'Peak Depths: Invasion\'')
    elif place == 'Blossom':
        if 'Blossom: Invasion' in completedInvasions:
            items, fishianGold = blossomAventure(Team, items, fishianGold)
        else:
            print('Dab\'s control is too strong! You can go here after completing \'Blossom: Invasion\'')
    return ded, gotGold, gotArco, metPizz, fishianGold, metIodine, gotMoreGold, borderCrossed, guardsDefeated, metEndurance, gotOrb, gotYay, metShale, valorAsked, andesiteRAWR, metCinnabar, gotIrn, items, fishFood


def fishTutorial():
    print("Welcome to Fishland")
    print("This is a place where fish live")
    print("But an evil fish has taken over the world")
    print("Will you save Fishland?")
    input('Press enter to continue. ')
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
    # urGenes = personAttributes(urName, "the Fish", random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(numlist), random.choice(gendlist), random.choice(colors), random.choice(colors), random.choice(colors))
    urGenes = makeoffspring(urMom, urDad)
    urName = urGenes.firstname
    createMoreFish(urName, "the Fish", urGenes, False)
    urFullName = urName + " the Fish"
    print("--Loading--")
    print(" ")
    input('Press enter to continue. ')
    print(" ")
    print("Hello! You are a fish!")
    print("Your name is " + urFullName + "!")
    print("You have a strength value of " + str(urGenes.strength) + ".")
    print("Strength is how strong your attack value is in fish-fights.")
    print("Your intelligence is " + str(urGenes.intelligence) + ", ")
    print("and your agility value is " + str(urGenes.agility) + ".")
    print("Intelligence is how smart you are, and agility is how fast you can run.")
    print("Your charisma(good looks) is " + str(urGenes.charisma) + ".")
    print("And finally your instinct value is " + str(urGenes.instinct) + ". ")
    print("This is how good you are at casting fishspells.")
    print("You are a " + urGenes.bodyColor + " fish with " + urGenes.finColor + " fins.")
    print("Your eyes are " + urGenes.eyeColor + ".")
    print("You are also a " + urGenes.gender + " fish.")
    return urName, urFullName


def storyline(urName):
    print(" ")
    print(" ")
    print("--Loading Game--")
    print(" ")
    input('Press enter to continue. ')
    print(" ")
    print("You blink open your eyes and see a sunrise-yellow fish by your side. ")
    print("Her loving dark-teal eyes watch you warmly.")
    print("\"I will name you " + urName + ".\" she says.")
    print("You see another, grass-green fish by you. She is munching on a strip of dried kelp.")
    print("\"" + urName + ", my name is Fidget. She is Kale.\" the sunrise-yellow fish says.")
    print("In fact, you are a special fish. ")
    print("You are one of the only fish left alive in a rebellion against Dab the Fish.")
    print("But can you rise up to the position of leader...")
    print("...and bring your army to the very ends of Dab's territory...")
    print("to lead you and the rebellion to success?")
    print(" ")
    print(" ")
    print('Years pass.')
    input(" ")
    print('You are now a juvenile fish, heady and strong.')
    print('Right now, the leader of the Kingdom is Tuple, a great fish.')
    print('One day right before you become an adult fish, a messenger comes rushing in.')
    print('\'Dab\'s troops detected at the border!\' the young fish shouts, worried.')
    print('Tuple\'s expression hardens. \'Call all troops. We will not go down without a fight.')
    print('He points a fin at you. \'You... stay here with Fidget, Bob, Sikell, and Carrot. Protect the camp.\'')
    print('After Tuple leaves with the rest of the fish, you look around.')
    print(
        '\'Well, since you\'re the most battle-experienced fish here, I trust you to make all the desicions.\' Fidget says.')
    print('\'Okayyy...\' you say. \'We can ready the defenses in case any fish comes near.\'')
    print('\'Carrot, go out on patrol. Fidget and Sikell\'The Boys\' can defend the frontlines, ')
    print('...and Bob and me can guard the camp border.\' you conclude.')
    print('The fish rush to their positions.')
    input(" ")
    print('A few minutes later, Fidget comes running back.')
    print('\'It\'s a fish, he has creepish purple eyes.\' Fidget says breathlessly.')
    print('\'He caught \'The Boys\' off guard, and now he\'s taken Carrot to his camp.\'')
    print('\'Tell all fish to stay back at the camp.\' you say. \'We need to protect ourselves.\'')
    print('Hours pass without anything.')
    print('Then you see a fish-- Kale. She is bloody and terribly wounded.')
    print('\'We lost. Tuple, Xenon, Angle and Cashmere died.\'')
    print('Fidget\'s eyes fill with tears. \'What about the rest?\'')
    print('\'Perimeter, Degree, and Sys ran off.\'')
    print('\'We don\'t know what happened to the others.\'')
    print('\'I guess, though,\' \'The Boys\' cuts in. \'then you are the leader, ' + urName + '.')
    input(" ")
    print('But there is no time to savor being the leader.')
    print('You have a kingdom to protect, and a tyrant to slay.')
    print('Your journey is just beginning.')
    print(' ')
    print(" ")
    addFish(fishArray, fidget)
    addFish(fishArray, kale)
    addFish(fishArray, theBoys_Sikell)
    addFish(fishArray, bob)

def splitprint(message):
    splitmessage = message.split()
    finalmessage = ' '.join(splitmessage)
    print(finalmessage)

def craft(item, fi, sg, w, c, s, m):
    if (item.fishianIron <= fi and item.seaGlass <= sg 
       and item.wood <= w and item.coral <= c
       and item.stone <= s and item.mineral <= s):
        items['Fishian Iron'][2] -= item.fishianIron
        items['Sea Glass'][2] -= item.seaGlass
        items['Wood'][2] -= item.wood
        items['Coral'][2] -= item.coral
        items['Stone'][2] -= item.stone
        items['Mineral'][2] -= item.mineral
        if not item.name == 'Arrow':
            items[item.name] = ['weapon', (item.name).lower(), random.randint(1, 10)]
        else:
            try: 
                items[item.name][2] += 2
            except KeyError as error:
                items[item.name] = ['weapon', 'arrow', 2]
    return items

def determineWin(losers, stage, nextstage, invasion):
    sortedLosers = losers
    sortedLosers.sort(reverse=True)
    if not sortedLosers[2] == 'you':
        if invasion == True and (not sortedLosers[3] == 'you'):
            print('You have completed \''+stage+'\'!')
            completedInvasions.append(stage)
            invasionsList.remove(stage)
        elif invasion == False:
            print('You have completed \''+stage+'\'!')
            completedInvasions.append(stage)
            invasionsList.append(stage+': Invasion')
            invasionsList.append(nextstage)
            invasionsList.remove(stage)
#    return completedInvasions, invasionsList

"""
Adding Stuff
if breedPowerfulFishAdded == 'no':
    missionArray['Breed a Powerful Fish'] = 'Breed a fish with base stats 38. Reward: 10 Fishian gold'
    breedPowerfulFishAdded = 'yes'
if crossBorderAdded == 'no':
    missionArray['Cross the Border'] = 'Cross the border to dangerous territory. Reward: 15 Fishian gold'
    crossBorderAdded = 'yes'
if defeatGuardsAdded == 'no':
    missionArray['Defeat Dab\'s Guards'] = 'Defeat the guards that have captured Silicon! Reward: 10 Fish Food'
    defeatGuardsAdded = 'yes'
if palaceBreakAdded == 'no':
    missionArray['Break into Dab\'s Palace'] = 'Break into Dab\'s Palace and assault him! Reward: 150 Fishian Gold'
    palaceBreakAdded = 'yes'
"""

ded = False
equippedItems = []
weapons = namedtuple('weapons', 'name, fishianIron, seaGlass, wood, coral, stone, mineral')
def theLoop(fishFood, fishianGold, fishMap, gotGold, kingdomStuff, items, ded):
    maxMapX = 47
    maxMapY = 22
    breedPowerfulFishAdded = 'no'
    crossBorderAdded = 'no'
    defeatGuardsAdded = 'no'
    palaceBreakAdded = 'no'
    findSiliconAdded = False
    fishlandMap = fishMap
    # (Cut-)Scenes
    akuScene = False
    kaleegg = False
    pifishborn = False
    triraborn = False
    while True:
        # Random scenes
        if random.randint(0, 10) == 1: # If the scene will even play
            if 'Akuma \'Aku\' Kelp' in fishArray and akuScene == False:
                print('Akuma heads in your direction.')
                print('\'Hey-\' she calls out. \'There\'s been something I\'ve wanted to tell you.\'')
                print('\'I had a friend- her name was Usagi-Ko.\'')
                print('\'Köyden had horribly injured her, and I\'m pretty sure she\'s dead')
                print('but it would do me some comfort to know she is still alive.\'')
                missionArray['Find Usagi-Ko'] = 'Find Akuma\'s long-gone friend, Usagi-Ko. Reward: Unknown'
                akuScene = True
            elif kaleegg == False:
                print('Kale and \'The Boys\' have mated and have fish-eggs.')
                kaleegg = True
            elif pifishborn == False:
                print('\'!!!\' you hear Kale scream. \'My eggs are hatching!\'')
                print('You quickly run over, to see two tiny fry.')
                print('\'I think I will name them (insert pi symbol) and Fish.\'')
                fish = personAttributes("Fish", "the Fish", 29, 38, 16, 19, 19, "Male", 0, 0, 0, kale, theBoys_Sikell)
                pi = personAttributes("π", "the Fish", 29, 38, 16, 19, 10, "Female", 0, 0, 0, kale, theBoys_Sikell)
                addFish(fishArray, pi)
                addFish(fishArray, fish)
                pifishborn = True
            
        while len(equippedItems) > 3:
            print('TOO.MANY.ITEMS')
        if ded == True:
            print('You are dead.')
            break
        yourKingdomStuff = kingdomStuff[0]
        cloudMountainStuff = kingdomStuff[1]
        mineralValleyStuff = kingdomStuff[2]
        peakDepthsStuff = kingdomStuff[3]
        gotGold = yourKingdomStuff[0]
        gotArco = yourKingdomStuff[1]
        metPizz = yourKingdomStuff[2]
        metIodine = yourKingdomStuff[3]
        gotMoreGold = cloudMountainStuff[0]
        borderCrossed = cloudMountainStuff[1]
        guardsDefeated = cloudMountainStuff[2]
        metEndurance = cloudMountainStuff[3]
        gotOrb = cloudMountainStuff[4]
        gotYay = cloudMountainStuff[5]
        metShale = mineralValleyStuff[0]
        valorAsked = mineralValleyStuff[1]
        andesiteRAWR = mineralValleyStuff[2]
        metCinnabar = peakDepthsStuff[0]
        print("These are your fish!")
        printDict(fishArray)
        print("These are your missions!")
        printDict(missionArray)
        print("These are your items!")
        printDict(items)
        print('You have ' + str(fishianGold) + ' Fishian gold,')
        print('and ' + str(fishFood) + ' fish food.')
        action = input("What would you like to do? breed, invade, adventure, hatch, look at items, craft, or mission?")
        action = action.lower()
        if action == 'hatch' or action == 'h':
            print("You can buy a fish egg for 100 Fishian gold!")
            if fishianGold >= 100:
                buy = input("Do you want to buy a fish egg? (y/n) ")
                if buy == "y":
                    fishianGold -= 100
                    print("Succeeded! You now have " + str(fishianGold) + " Fishian gold.")
                    try:
                        items['fishEgg'][2] += 1
                    except KeyError as error:
                        items['fishEgg'] = ['egg', 'fish', 1]
            else:
                print("You do not have enough Fishian gold.")
                print("You can trade for Fish Food and Fishian gold with Endurance, who resides by the mountains.")
        elif action == 'breed' or action == 'b':
            print("You can breed two fish!")
            print("It costs 38 food to breed two fish.")
            if fishFood >= 38:
                if input("Do you wish to do so?(y/n) ") == "y":
                    fishFood -= 38
                    myNewFish = createFromAquarium()
                    print('Succeeded! The fish is coming...')
                    print('Your fish is here!')
                    addFish(fishArray, myNewFish)
                    print(myNewFish)

            else:
                print("You don't have enough fish food.")
                if findSiliconAdded == False:
                    print("Purchase fish food from Silicon, who lives by the border, in hostile territory.")
                    missionArray['Find Silicon'] = 'Journey to the border to find Silicon. Reward: 200 Fish Food'
                    findSiliconAdded = True
                else:
                    print('You can trade Fish Food and Fishian gold with Endurance, who resides by the mountain.')
        elif action == 'mission' or action == 'm':
            print('You can try to complete a mission!')
            missions = missionArray.keys()
            print('These are your mission-names')
            print(missions)
            print(
                'Please enter the name of the mission you want to complete.\n If you have already completed the mission, you will recieve the reward.')
            whichMission = input(' ')
            if whichMission in missions:
                if whichMission == 'Defeat Dab':
                    if (('Cross the Border' in completedMissions) and (
                            'Breed a Powerful Fish' in completedMissions) and (
                            'Break into Dab\'s Palace' in completedMissions)):
                        print('You have completed this mission.')
                        # ending
                        completedMissions['Defeat Dab'] = missionArray['Defeat Dab']
                        del missionArray['Defeat Dab']
                        continue
                    print(
                        'To complete this mission, you must complete the missions \n \'Breed a Powerful Fish\', \'Cross the Border\', and more.')
                    if breedPowerfulFishAdded == 'no':
                        missionArray[
                            'Breed a Powerful Fish'] = 'Breed a fish with base stats 38. Reward: 99 Fishian gold'
                        breedPowerfulFishAdded = 'yes'
                    if crossBorderAdded == 'no':
                        missionArray[
                            'Cross the Border'] = 'Cross the border to dangerous territory. Reward: 15 Fishian gold'
                        crossBorderAdded = 'yes'
                    if palaceBreakAdded == 'no':
                        missionArray[
                            'Break into Dab\'s Palace'] = 'Break into Dab\'s Palace and assault him! Reward: 150 Fishian Gold'
                        palaceBreakAdded = 'yes'
                elif whichMission == 'Find Silicon':
                    if 'Cross the Border' in completedMissions and 'Defeat Dab\'s Guards' in completedMissions:
                        print('You have completed this mission!')
                        fishFood += 200
                        print('You have received 200 Fish Food!')
                        print('Now, you have ' + str(fishFood) + ' Fish Food!')
                        completedMissions['Find Silicon'] = missionArray['Find Silicon']
                        del missionArray['Find Silicon']
                        continue
                    print(
                        'To complete this mission, you must complete the missions \'Cross the Border\' and \'Defeat Dab\'s guards\'.')
                    if crossBorderAdded == 'no':
                        missionArray[
                            'Cross the Border'] = 'Cross the border to dangerous territory. Reward: 15 Fishian gold'
                        crossBorderAdded = 'yes'
                    if defeatGuardsAdded == 'no':
                        missionArray[
                            'Defeat Dab\'s Guards'] = 'Defeat the guards that have captured Silicon! Reward: Something Special'
                        defeatGuardsAdded = 'yes'
                elif whichMission == 'Breed a Powerful Fish':
                    # make function to determine if there is a fish
                    print('To complete this mission, you must breed a fish who has strength 38, ')
                    print('intelligence 38, agility 38, charisma 38, and instinct 38, which is the highest value.')
                    print('You can breed and hatch fish eggs to do this.')
                    print('You can enter \'breed\' or \'hatch\' on the main-input.')
                elif whichMission == 'Cross the Border':
                    if borderCrossed == True:
                        print('You have completed this mission!')
                        fishianGold += 15
                        print('You have recieved 15 Fishian gold!')
                        print('Now, you have ' + str(fishianGold) + ' Fishian gold!')
                        completedMissions['Cross the Border'] = missionArray['Cross the Border']
                        del missionArray['Cross the Border']
                    print(
                        'To complete this mission, you must cross Dab\'s border, anywhere,\n as long as you cross it.')
                    print('You can cross the border in the \'adventure\' tab in the main-screen.')
                elif whichMission == 'Defeat Dab\'s Guards':
                    if (guardsDefeated == True) and ('Cross the Border' in completedMissions):
                        print('You have completed this mission!')
                        items['Köyden\'s Perseverance'] = ['spirit', 'köyden', 'evda']
                        print('You have recieved a spirit. Check it out in the Items tab!')
                        completedMissions['Defeat Dab\'s Guards'] = missionArray['Defeat Dab\'s Guards']
                        del missionArray['Defeat Dab\'s Guards']
                    print('To complete this mission, you must first cross the border.')
                    print('Then, you must defeat the guards(duh). Check the Adventure tab.')
                    if crossBorderAdded == 'no':
                        missionArray[
                            'Cross the Border'] = 'Cross the border to dangerous territory. Reward: 15 Fishian gold'
                        crossBorderAdded = 'yes'
                elif whichMission == 'Find Lime':
                    if limeFound == True:
                        print('You have completed this mission!')
                        items['Shale Ore'] = ['ore', 'shale', 'shale']
                        print('You have recieved a piece of shale ore! Check it out in the Items tab!')
                        completedMissions['Find Lime'] = missionArray['Find Lime']
                        del missionArray['Find Lime']
                    print('To complete this mission, you must find Lime the Fish.')
                elif whichMission == 'Find Usagi-Ko':
                    if usaFound == True:
                        print('You have completed this mission!')
                        items['Usagi-Ko\'s Staff'] = ['staff', 'luminite', 28]
                        print('You have recieved Usagi-Ko\'s Staff! Check it out in the Items tab!')
                        completedMissions['Find Usagi-Ko'] = missionArray['Find Usagi-Ko']
                        del missionArray['Find Usagi-Ko']
                    print('To complete this mission, you must find Usagi-Ko Chisai.')
            else:
                print('This mission does not exist or is already completed! (or is a typo.)')
                continue
        elif action == 'adventure' or action == 'a':
            print('ADVENTURE in Fishland!')
            printMap(fishlandMap)
            input('Press enter to continue.')
            print('Where would you like to go?')
            print('This is the key to the map.')
            printDict(adventurePlaces)
            destinationX = input('Please choose a destination! Enter the x-coordinate. ')
            try:
                destinationX = int(destinationX)
            except ValueError as error:
                print('That is not an integer!')
                continue
            destinationY = input('Please choose a destination! Enter the y-coordinate. ')
            try:
                destinationY = int(destinationY)
            except ValueError as error:
                print('That is not an integer!')
                continue
            if destinationX <= maxMapX and destinationY <= maxMapY:
                newMap = assignXY(fishlandMap, destinationX, destinationY, '🟥')
                printMap(newMap)
                print('Is this where you want to go??')
                approval = input()
                approval = approval.lower()
                approval = approval + 'placeholder'
                if approval[0] == 'y':
                    print('Thank you! We shall adventure here!')
                    adventurePlace = findPlace(destinationX, destinationY)
                    print('You are adventuring in ' + str(adventurePlace) + '!')
                    fishTeam = fishAdventure(adventurePlace, urFullName)
                    global completedInvasions
                    ded, gotGold, gotArco, metPizz, fishianGold, metIodine, gotMoreGold, borderCrossed, guardsDefeated, metEndurance, gotOrb, gotYay, metShale, valorAsked, andesiteRAWR, metCinnabar, gotIrn, items, fishFood = trueAdventure(
                        fishianGold, fishFood, fishTeam, adventurePlace, kingdomStuff, items, completedInvasions)
                    yourKingdomStuff = [gotGold, gotArco, metPizz, metIodine]
                    cloudMountainStuff = [gotMoreGold, borderCrossed, guardsDefeated, metEndurance, gotOrb, gotYay]
                    mineralValleyStuff = [metShale, valorAsked, andesiteRAWR]
                    peakDepthsStuff = [metCinnabar, gotIrn]
                    kingdomStuff = [yourKingdomStuff, cloudMountainStuff, mineralValleyStuff, peakDepthsStuff]
        elif action == 'look at items' or action == 'l':
            printDict(items)
            item = input('What item do you want to look at?')
            if item in items.keys():
                print('This Item Exists!!')
                print('Sorry, the item update is not on yet. Check later versions.')
                if items[item][0] == 'orb':
                    print('A orb is a type of item that can elevate a fish\'s base stat.')
                    print('This orb can elevate '+items[item][1]+' by '+str(items[item][2])+'.')
                elif items[item][0] == 'weapon':
                    print('A weapon is a item that can make an attack deal more damage.')
                    print('This weapon is a '+items[item][1]+' that can raise attack by '+str(items[item][2])+'.')
                elif items[item][0] == 'ingredient':
                    print('A ingredient is similar to a material, but is used mainly in potions and elixirs.')
                    print('This ingredient is a piece of '+items[item][2]+' '+items[item][1]+'.')
                    if items[item][1] == 'coral':
                        if items[item][2] == 'kydian':
                            print('Kydian coral is one of the key ingredients of the Immortality potion.')
                    elif items[item][1] == 'stone':
                        if items[item][2] == 'chisian':
                            print('Chisian stone, otherwise known as Nyachi, is the other key ingredient in the Immortality potion.')
                elif items[item][0] == 'material':
                    print('A material is a thing that is used to craft things such as swords daggers and staffs.')
                    print('This is a piece of '+items[item][1]+'. You have '+str(items[item][i])+' of it.')
                if item not in equippedItems and item[items][0] != 'ingredient' and item[items][0] != 'material':
                    equip = input('Equip this item? ')
                    equip = equip + 'placeholder'
                    if equip[0] == 'y':
                        equippedItems.append(item)
        elif action == 'invade' or action == 'i':
            print('''	Invasions 101
            Invasions are rounds of 4 battles in which
            when your team wins, you unlock either a new
            Invasion stage or access to a Adventuring region.''')
            global invasionsList
            print(invasionsList)
            print('These are the list of stages you can challenge.')
            stage = input('Which stage would you like to challenge? ')
            if stage in invasionsList:
                print('Invasion!')
                invasionTeam = []
                while len(invasionTeam) < 4:
                    fish = ''
                    while fish not in fishArray:
                        fish = input('Which fish do you want to bring? (Enter in full.) ')
                    invasionTeam.append(fish)
                splitprint(stage)
                print('In this stage, you must fight some fish. (duh)')
                input('Ready? ')
                input('Set: ')
                input('GO!!')
                random.shuffle(invasionTeam)
                losers = []
                # Normal Stages
                if stage == 'Cloud Mountains':
                    for i in range(len(invasionTeam)):
                        print('ROUND '+str(i))
                        print(invasionTeam[i]+' VS Guard')
                        guard = personAttributes('Random', 'Guard', random.choice(numlist), random.choice(numlist),
                                      random.choice(numlist), random.choice(numlist), random.choice(numlist),
                                      random.choice(gendlist), random.choice(colors), random.choice(colors),
                                      random.choice(colors), None, None)
                        breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, guard, 200, 200, normalEnemyStratagems)
                        losers.append(loser)
                    determineWin(losers, stage, 'Mineral Valley', False)
                elif stage == 'Mineral Valley':
                    for i in range(len(invasionTeam)):
                        print('ROUND '+str(i))
                        print(invasionTeam[i]+' VS Guard')
                        nums = range(3, 19)
                        guard = personAttributes('Random', 'Guard', random.choice(numlist), random.choice(numlist),
                                      random.choice(nums), random.choice(numlist), random.choice(numlist),
                                      random.choice(gendlist), random.choice(colors), random.choice(colors),
                                      random.choice(colors), None, None)
                        breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, guard, 200, 200, normalEnemyStratagems)
                        losers.append(loser)
                    determineWin(losers, stage, 'Peak Depths', False)

                elif stage == 'Peak Depths':
                    for i in range(len(invasionTeam)):
                        print('ROUND '+str(i))
                        print(invasionTeam[i]+' VS Guard')
                        nums = range(8, 20)
                        guard = personAttributes('Random', 'Guard', random.choice(numlist), random.choice(numlist),
                                      random.choice(nums), random.choice(numlist), random.choice(numlist),
                                      random.choice(gendlist), random.choice(colors), random.choice(colors),
                                      random.choice(colors), None, None)
                        breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, guard, 200, 200, normalEnemyStratagems)
                    completedInvasions, invasionsList = determineWin(losers, stage, 'THIS STAGE DOES NOT EXIST', False)
                # Invasion Stages
                elif stage == 'Cloud Mountains: Invasion':
                    for i in range(len(invasionTeam) - 1):
                        print('ROUND '+str(i))
                        print(invasionTeam[i]+' VS Guard')
                        guard = personAttributes('Random', 'Guard', random.choice(numlist), random.choice(numlist),
                                      random.choice(numlist), random.choice(numlist), random.choice(numlist),
                                      random.choice(gendlist), random.choice(colors), random.choice(colors),
                                      random.choice(colors), None, None)
                        breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, guard, 200, 200, normalEnemyStratagems)
                        losers.append(loser)
                    print('ROUND 3')
                    print(invasionTeam[i-1]+' VS General Kobuta')
                    kobuta = personAttributes('Kobuta', 'Chisai', 18, 32, 13, 7, 15, 'Male', 'crimson', 'carmine', 'sea blue', None, None)
                    breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, kobuta, 200, 400, normalEnemyStratagems)
                    losers.append(loser)
                    determineWin(losers, stage, None, True)
                elif stage == 'Mineral Valley: Invasion':
                    for i in range(len(invasionTeam) - 1):
                        print('ROUND '+str(i))
                        print(invasionTeam[i]+' VS Guard')
                        nums = range(6, 19)
                        guard = personAttributes('Random', 'Guard', random.choice(numlist), random.choice(numlist),
                                      random.choice(nums), random.choice(numlist), random.choice(numlist),
                                      random.choice(gendlist), random.choice(colors), random.choice(colors),
                                      random.choice(colors), None, None)
                        breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, guard, 200, 200, normalEnemyStratagems)
                        losers.append(loser)
                    print('ROUND 3')
                    print(invasionTeam[i-1]+' VS Warrior Starlight')
                    starlight = personAttributes('Starlight', 'Kelp', 18, 30, 17, 16, 8, 'Female', 'dark gray', 'dark gray', 'sunrise yellow', None, None)
                    breakForUnMutation, loser = battle(fishArray[invasionTeam[i-1]], 200, 200, starlight, 200, 400, normalEnemyStratagems)
                    losers.append(loser)
                    determineWin(losers, stage, None, True)
        elif action == 'craft' or action == 'c':
            splitprint('CRAFT')
            print('''		Crafting 101
            To craft a item is to combine several materials to create
            a weapon or item.''')
            # remember weapons(name, fishianIron, seaGlass, wood, coral, stone, mineral)
            _Knife = weapons('Knife', 2, 4, 0, 1, 2, 0)
            Dagger = weapons('Dagger', 3, 3, 0, 2, 0, 1)
            ___Bow = weapons('Bow', 1, 3, 5, 0, 1, 0)
            Arrow2 = weapons('Arrow', 2, 0, 2, 2, 3, 1)
            _Staff = weapons('Staff', 0, 2, 0, 0, 6, 1)
            _Spear = weapons('Spear', 7, 1, 0, 7, 0, 0)
            Fishian_Iron = items['Fishian Iron'][2]
            Sea_Glass = items['Sea Glass'][2]
            Wood = items['Wood'][2]
            Coral = items['Coral'][2]
            Stone = items['Stone'][2]
            Mineral = items['Mineral'][2]
            crafts = {'Knife': _Knife, 
                     'Dagger': Dagger, 
                     'Bow': ___Bow,
                     '2 Arrows': Arrow2,
                     'Staff': _Staff,
                     'Spear': _Spear}
            printDict(crafts)
            print('You have '+str(Fishian_Iron)+' Fishian iron, '+str(Sea_Glass)+' sea glass, ')
            print(str(Wood)+' wood, '+str(Coral)+' coral, '+str(Stone)+' stone, and '+str(Mineral)+' mineral.')
            what = input('What would you like to craft? Enter in full. ')
            if what in crafts.keys():
                items = craft(crafts[what], Fishian_Iron, Sea_Glass, Wood, Coral, Stone, Mineral)
        else:
            break


print(title)
"""
testprogram()
makeNewFish()
createFish()
fish = createFromAquarium()
print(fish)
print(fishArray)
"""

print("Hello! This is a game of breeding fish.")
gameType = input("New game?(y/n) ")
if gameType == "y":
    urName, urFullName = fishTutorial()
    storyline(urName)
    theLoop(fishFood, fishianGold, fishMap, gotGold, kingdomStuff, items, ded)

# elif gameType == "n":
#    pass
else:
    print("Invalid input!")
    printMap(fishMap)
    battle(fidget, 200, 200, bob, 200, 200, normalEnemyStratagems)
