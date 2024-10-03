title = "Anagramatical"
def anagram(letterlist):  #test
    usedstrings = []
    counter = 0
    if len(letterlist) > 1:
        for i in letterlist:
            letterlist2 = letterlist.copy()
            letterlist2.pop(letterlist2.index(i))
            if len(letterlist) > 2:
                for l in letterlist2:
                    letterlist3 = letterlist.copy()
                    letterlist3.pop(letterlist3.index(i))
                    letterlist3.pop(letterlist3.index(l))
                    if len(letterlist) > 3:
                        for e in letterlist3:
                            letterlist4 = letterlist.copy()
                            letterlist4.pop(letterlist4.index(i))
                            letterlist4.pop(letterlist4.index(l))
                            letterlist4.pop(letterlist4.index(e))
                            if len(letterlist) > 4:
                                for t in letterlist4:
                                    letterlist5 = letterlist.copy()
                                    letterlist5.pop(letterlist5.index(i))
                                    letterlist5.pop(letterlist5.index(l))
                                    letterlist5.pop(letterlist5.index(e))
                                    letterlist5.pop(letterlist5.index(t))
                                    if len(letterlist) > 5:
                                        for r in letterlist5:
                                            letterlist6 = letterlist.copy()
                                            letterlist6.pop(letterlist6.index(i))
                                            letterlist6.pop(letterlist6.index(l))
                                            letterlist6.pop(letterlist6.index(e))
                                            letterlist6.pop(letterlist6.index(t))
                                            letterlist6.pop(letterlist6.index(r))
                                            if len(letterlist) > 6:
                                                for s in letterlist6:
                                                    letterlist7 = letterlist.copy()
                                                    letterlist7.pop(letterlist7.index(i))
                                                    letterlist7.pop(letterlist7.index(l))
                                                    letterlist7.pop(letterlist7.index(e))
                                                    letterlist7.pop(letterlist7.index(t))
                                                    letterlist7.pop(letterlist7.index(r))
                                                    letterlist7.pop(letterlist7.index(s))
                                                    if len(letterlist) > 7:
                                                        for a in letterlist7:
                                                            letterlist8 = letterlist.copy()
                                                            letterlist8.pop(letterlist8.index(i))
                                                            letterlist8.pop(letterlist8.index(l))
                                                            letterlist8.pop(letterlist8.index(e))
                                                            letterlist8.pop(letterlist8.index(t))
                                                            letterlist8.pop(letterlist8.index(r))
                                                            letterlist8.pop(letterlist8.index(s))
                                                            letterlist8.pop(letterlist8.index(a))
                                                            if len(letterlist) > 8:
                                                                for g in letterlist8:
                                                                    letterlist9 = letterlist.copy()
                                                                    letterlist9.pop(letterlist9.index(i))
                                                                    letterlist9.pop(letterlist9.index(l))
                                                                    letterlist9.pop(letterlist9.index(e))
                                                                    letterlist9.pop(letterlist9.index(t))
                                                                    letterlist9.pop(letterlist9.index(r))
                                                                    letterlist9.pop(letterlist9.index(s))
                                                                    letterlist9.pop(letterlist9.index(a))
                                                                    letterlist9.pop(letterlist9.index(g))
                                                                    if len(letterlist) > 9:
                                                                        for y in letterlist9:
                                                                            letterlist0 = letterlist.copy()
                                                                            letterlist0.pop(letterlist0.index(i))
                                                                            letterlist0.pop(letterlist0.index(l))
                                                                            letterlist0.pop(letterlist0.index(e))
                                                                            letterlist0.pop(letterlist0.index(t))
                                                                            letterlist0.pop(letterlist0.index(r))
                                                                            letterlist0.pop(letterlist0.index(s))
                                                                            letterlist0.pop(letterlist0.index(a))
                                                                            letterlist0.pop(letterlist0.index(g))
                                                                            letterlist0.pop(letterlist0.index(y))
                                                                            if len(letterlist) > 10:
                                                                                print('The system can\'t handle a 10+ character chain! Shorter please...')
                                                                            else:
                                                                                for p in letterlist0:
                                                                                    string = i+l+e+t+r+s+a+g+y+p
                                                                                    if string not in usedstrings:
                                                                                        print(string)
                                                                                        counter+=1
                                                                                        usedstrings.append(string)
                                                                    else:
                                                                        for y in letterlist9:
                                                                            string = i+l+e+t+r+s+a+g+y
                                                                            if string not in usedstrings:
                                                                                print(string)
                                                                                counter+=1
                                                                                usedstrings.append(string)
                                                            else:
                                                                for g in letterlist8:
                                                                    string = i+l+e+t+r+s+a+g
                                                                    if string not in usedstrings:
                                                                        print(string)
                                                                        counter+=1
                                                                        usedstrings.append(string)
                                                    else:
                                                        for a in letterlist7:
                                                            string = i+l+e+t+r+s+a
                                                            if string not in usedstrings:
                                                                print(string)
                                                                counter+=1
                                                                usedstrings.append(string)
                                            else:
                                                for s in letterlist6:
                                                    string = i+l+e+t+r+s
                                                    if string not in usedstrings:
                                                        print(string)
                                                        counter+=1
                                                        usedstrings.append(string)
                                    else:
                                        for r in letterlist5:
                                            string = i+l+e+t+r
                                            if string not in usedstrings:
                                                print(string)
                                                counter+=1
                                                usedstrings.append(string)
                            else:
                                for t in letterlist4:
                                    string = i+l+e+t
                                    if string not in usedstrings:
                                        print(string)
                                        counter+=1
                                        usedstrings.append(string)
                    else:
                        for e in letterlist3:
                            string = i+l+e
                            if string not in usedstrings:
                                print(string)
                                counter+=1
                                usedstrings.append(string)
            else:
                for l in letterlist2:
                    string = i+l
                    if string not in usedstrings:
                        print(string)
                        counter+=1
                        usedstrings.append(string)
    else:
        print(letterlist[0])
        counter+=1
    print('Total number of anagrams: '+str(counter))

              
print(title)
word = input('Which word would you like to anagram? ')
letterlist = [char for char in word]
anagram(letterlist)
