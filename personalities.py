import random
fishies = []
print('Which fish are you?')
print('')
print('')
print('I. Who is your most hated antagonist?')
print('(A) Dab the Fish')
print('(B) Köyden Kyda')
print('(C) Andesite Kelp')
print('(D) Shard the Fish')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Shif')
    elif answer == 'b':
        fishies.append('Akuma')
    elif answer == 'c':
        fishies.append('Cinder')
    else:
        fishies.append('Köyden')
print(answer)
print('(Oh, don\'t mind that, it\'s just a syntax thing)')

print('')
print('II. What do you do in your free time?')
print('(A) Beat up a sibling')
print('(B) Read')
print('(C) Draw')
print('(D) Play video games')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Dab')
        fishies.append('Starlight')
    elif answer == 'b':
        fishies.append('Usagi-Ko')
        fishies.append('Kale')
    elif answer == 'c':
        fishies.append('Fidget')
    else:
        fishies.append('Hope')

print('')
print('III. How do you like to fight?')
print('(A) With a close-range weapon')
print('(B) With a long-range weapon')
print('(C) I don\'t fight, others do it for me')
print('(D) I prefer to meditate')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Shif')
        fishies.append('Köyden')
    elif answer == 'b':
        fishies.append('Fabbit')
    elif answer == 'c':
        fishies.append('Yay')
        fishies.append('Dab')
    else:
        fishies.append('Usagi-Ko')
        fishies.append('Kitsune-Ko')

print('')
print('IV. How many friends do you have?')
print('(A) Lots')
print('(B) A few')
print('(C) Only one')
print('(D) Absolutely none: I am a loner')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Hope')
        fishies.append('Kale')
    elif answer == 'b':
        fishies.append('Fidget')
    elif answer == 'c':
        fishies.append('Akuma')
        fishies.append('Iodine')
    else:
        fishies.append('Köyden')
        fishies.append('Shard')

print('')
print('V. How many former girl/boyfriends do you have?')
print('(A) None, I haven\'t ever had one')
print('(B) None, my first is still going great with me!')
print('(C) A few')
print('(D) Far too many for my liking')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Köyden')
    elif answer == 'b':
        fishies.append('Shif')
        fishies.append('Fidget')
    elif answer == 'c':
        fishies.append('Pizzicato')
        fishies.append('Cygnet')
    else:
        fishies.append('Dab')

print('')
print('VI. Where do you pick your fights?')
print('(A) On the school field')
print('(B) In the classroom/office')
print('(C) On abandoned plains')
print('(D) In dark stone quarries')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Pizzicato')
        fishies.append('Iodine')
    elif answer == 'b':
        fishies.append('Hope')
        fishies.append('Kale')
    elif answer == 'c':
        fishies.append('Artemis')
        fishies.append('Cygnet')
    else:
        fishies.append('Köyden')
        fishies.append('Arch')

print('')
print('VII. How do you like your magic?')
print('(A) Lots of power! Haha!')
print('(B) In a staff, where it\'s safe')
print('(C) Umm...like...more internal-ish?')
print('(D) Anything that\'s not like it is now.')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Dab')
    elif answer == 'b':
        fishies.append('Usagi-Ko')
    elif answer == 'c':
        fishies.append('Artemis')
    else:
        fishies.append('Axis')
        fishies.append('Cygnet')
        fishies.append('Arch')

print('')
print('VIII. What is your favorite kind of curse?')
print('(A) Wormhole(time)')
print('(B) Warp(space)')
print('(C) Immortality(a curse in its own way)')
print('(D) Mutation(undead)')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Artemis')
    elif answer == 'b':
        fishies.append('Cygnet')
    elif answer == 'c':
        fishies.append('Axis')
    else:
        fishies.append('Dab')

print('')
print('IX. What kind of crown would you have if you did?')
print('(A) Elaborate, with tons of jewels and gold')
print('(B) Simple and light, easy to wear')
print('(C) Just a simple gold crown')
print('(D) I don\'t deserve one anyways, why should I?')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Dab')
    elif answer == 'b':
        fishies.append('Andesite')
    elif answer == 'c':
        fishies.append('Arch')
    else:
        fishies.append('Köyden')

print('')
print('X. Who is the most annoying protoganist?')
print('(A) Hope the Fish')
print('(B) Cygnet Cardinal')
print('(C) Artemis Kyda')
print('(D) Mona Forieh')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Kale')
    elif answer == 'b':
        fishies.append('Artemis')
        fishies.append('Arch')
    elif answer == 'c':
        fishies.append('Cygnet')
    else:
        fishies.append('Hope')

# Results
def organize(thelist):
    thedict = {}
    for i in thelist:
        if i in thedict.keys():
            thedict[i] += 1
        else:
            thedict[i] = 1
    return thedict
def maximum(thelist, maxnum, leverage):
    checkagain = []
    for i in thelist:
        if i == maxnum:
            checkagain.append(i)
        elif i > maxnum:
            maxnum = i
    if leverage == 10:
        while True:
            print('FunctionError: Function recall too many times')
            print('(In other words: restart the program!!!)')
    else:
        if len(checkagain) > 0:
            leverage += 1
            maxnum = maximum(checkagain, maxnum, leverage)
    return maxnum

def check(keys, values, dic):
    newkeys = []
    newvalues = []
    for i in range(len(keys)):
        newkeys.append(keys[i-1])
        if dic[keys[i-1]] == values[i-1]:
            newvalues.append(values[i-1])
        else:
            newvalues.append(dic[keys[i-1]])
    return newkeys, newvalues

fishiesdict = organize(fishies)
print(fishies)
print(fishiesdict)
KEYS = list(fishiesdict.keys())
VALUES = list(fishiesdict.values())
maxnum = maximum(VALUES, 0, 1)
print(KEYS)
print(VALUES)
KEYS, VALUES = check(KEYS, VALUES, fishiesdict)
print(KEYS)
print(VALUES)
fishindex = VALUES.index(maxnum)
yourfish = KEYS[fishindex]
print("You are "+yourfish+"!")
