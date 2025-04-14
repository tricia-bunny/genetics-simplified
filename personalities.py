import random
fishies = []
print('Which fish are you?')
print('')
print('')
print('I. Who is your most hated antagonist?')
print('(A) Dab the Fish')
print('(B) Köyden Kyda')
print('(C) Myself... :(')
print('(D) Shard the Fish')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Shif')
        fishies.append('Andesite')
        fishies.append('Kale')
    elif answer == 'b':
        fishies.append('Akuma')
        fishies.append('Hope')
        fishies.append('Shard')
    elif answer == 'c':
        fishies.append('Usagi-Ko')
        fishies.append('Cygnet')
        fishies.append('Skylon')
    else:
        fishies.append('Köyden')
        fishies.append('Vivo')
        fishies.append('Ji\'Xiang')
print(answer)
print('(Oh, don\'t mind that, it\'s just a syntax thing)')

print('')
print('II. What do you do in your free time?')
print('(A) Beat up a sibling')
print('(B) Read')
print('(C) Think of Strategic Plans')
print('(D) Play video games')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Shif')
        fishies.append('Skylon')
        fishies.append('Andesite')
    elif answer == 'b':
        fishies.append('Cygnet')
        fishies.append('Kale')
        fishies.append('Akuma')
    elif answer == 'c':
        fishies.append('Köyden')
        fishies.append('Usagi-Ko')
        fishies.append('Shard')
    else:
        fishies.append('Hope')
        fishies.append('Ji\'Xiang')
        fishies.append('Vivo')

print('')
print('III. How do you like to fight?')
print('(A) With a close-range weapon')
print('(B) With a long-range weapon')
print('(C) I don\'t fight, others do it for me')
print('(D) I prefer to meditate')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Andesite')
        fishies.append('Köyden')
        fishies.append('Ji\'Xiang')
    elif answer == 'b':
        fishies.append('Kale')
        fishies.append('Vivo')
        fishies.append('Shif')
    elif answer == 'c':
        fishies.append('Hope')
        fishies.append('Shard')
        fishies.append('Skylon')
    else:
        fishies.append('Usagi-Ko')
        fishies.append('Cygnet')
        fishies.append('Akuma')

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
        fishies.append('Skylon')
    elif answer == 'b':
        fishies.append('Ji\'Xiang')
        fishies.append('Cygnet')
        fishies.append('Andesite')
    elif answer == 'c':
        fishies.append('Akuma')
        fishies.append('Iodine')
        fishies.append('Shif')
    else:
        fishies.append('Köyden')
        fishies.append('Shard')
        fishies.append('Vivo')

print('')
print('V. Would you end your life to save another?')
print('(A) Yes')
print('(B) No, I value my own life more')
print('(C) If that person was important to me')
print('(D) No, it would only be temporary anyway')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Kale')
        fishies.append('Akuma')
        fishies.append('Usagi-Ko')
    elif answer == 'b':
        fishies.append('Shard')
        fishies.append('Vivo')
        fishies.append('Köyden')
    elif answer == 'c':
        fishies.append('Hope')
        fishies.append('Shif')
        fishies.append('Ji\'Xiang')
    else:
        fishies.append('Skylon')
        fishies.append('Cygnet')
        fishies.append('Andesite')

print('')
print('VI. All your friends are dead.')
print('(A) Commit suicide so I can be with them again')
print('(B) I killed them all')
print('(C) Avenge them!')
print('(D) Move on and find new ones. Friends are only fleeting.')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Akuma')
        fishies.append('Andesite')
        fishies.append('Kale')
    elif answer == 'b':
        fishies.append('Köyden')
        fishies.append('Shard')
        fishies.append('Skylon')
    elif answer == 'c':
        fishies.append('Hope')
        fishies.append('Ji\'Xiang')
        fishies.append('Vivo')
    else:
        fishies.append('Cygnet')
        fishies.append('Usagi-Ko')
        fishies.append('Shif')

print('')
print('VII. What would you change about yourself?')
print('(A) My past betrayals')
print('(B) Nothing')
print('(C) My past mistakes')
print('(D) My past failures')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Usagi-Ko')
        fishies.append('Köyden')
        fishies.append('Andesite')
    elif answer == 'b':
        fishies.append('Shif')
        fishies.append('Kale')
        fishies.append('Ji\'Xiang')
    elif answer == 'c':
        fishies.append('Cygnet')
        fishies.append('Hope')
        fishies.append('Kale')
    else:
        fishies.append('Skylon')
        fishies.append('Shard')
        fishies.append('Vivo')

print('')
print('VIII. What do you take as your victory reward?')
print('(A) The head of the enemy leader')
print('(B) Nothing')
print('(C) Recognition')
print('(D) Freedom')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Shard')
        fishies.append('Vivo')
        fishies.append('Akuma')
    elif answer == 'b':
        fishies.append('Usagi-Ko')
        fishies.append('Shif')
        fishies.append('Kale')
    elif answer == 'c':
        fishies.append('Hope')
        fishies.append('Ji\'Xiang')
        fishies.append('Skylon')
    else:
        fishies.append('Köyden')
        fishies.append('Andesite')
        fishies.append('Cygnet')

print('')
print('IX. What would you describe yourself as?')
print('(A) Traitor')
print('(B) Unworthy')
print('(C) Insignificant')
print('(D) Unempathetic')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Köyden')
        fishies.append('Usagi-Ko')
        fishies.append('Andesite')
    elif answer == 'b':
        fishies.append('Ji\'Xiang')
        fishies.append('Shif')
        fishies.append('Andesite')
    elif answer == 'c':
        fishies.append('Cygnet')
        fishies.append('Kale')
        fishies.append('Vivo')
    else:
        fishies.append('Shard')
        fishies.append('Akuma')
        fishies.append('Skylon')

print('')
print('X. What is immortality?')
print('(A) The greatest curse of all')
print('(B) A blessing from the gods')
print('(C) A two-sided sword')
print('(D) An unachievable, insignificant dream')
answer = input('').lower()
if answer in ['a', 'b', 'c', 'd']:
    if answer == 'a':
        fishies.append('Cygnet')
        fishies.append('Usagi-Ko')
        fishies.append('Akuma')
    elif answer == 'b':
        fishies.append('Shard')
        fishies.append('Hope')
        fishies.append('Kale')
    elif answer == 'c':
        fishies.append('Shif')
        fishies.append('Ji\'Xiang')
        fishies.append('Vivo')
    else:
        fishies.append('Köyden')
        fishies.append('Andesite')
        fishies.append('Skylon')

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
