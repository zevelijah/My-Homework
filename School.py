# %%
# Problem 1.3
# It is assumed that their is space for the added text
def Spacer(sent, leg):
    wer = 0
    wer1 = 0
    for x in sent:
        wer += 1
        wer1 += 1
        if x == ' ':
            cut = sent[:wer]
            print(f"{ cut }")
            sent = sent.replace(cut, '', 1)
            print(f"sent: { sent }")
            cut0 = cut[:-1]+ '%20'
            print(f"cut0:{ cut0 }")
            sent = cut0 + sent
            wer += 2
        if leg == wer1:
            break
    return sent
pla = Spacer('Mr John Smith     ', 13)
print(pla)
# %%
# problem 1.6
# letters only
print("space")
def stringCompression(string):
    stand = None
    count = 0
    f = 0
    newString = ''
    first = True
    for let in string:
        f += 1
        if first == False:
            if let == stand:
                count += 1
            else:
                newString = newString + f"{ stand }{ count }"
                stand = let
                count = 1
            if f == len(string):
                newString = newString + f"{ stand }{ count }" 
        else:
            count += 1
            stand = let
            first = False
    if len(newString) >= len(string):
        return string, 'The funcition is no use for this.'
    else:
        return newString
compresed = stringCompression('aaabbbbccccsa')
other = stringCompression('aas')
print(compresed)
print(other)
# %%
# FOR CHEMISTRY
print("space")
def molesPerKilo(kilos, a, am, b, bm, c, cm):
    grams = kilos * 1000
    aam = a * am + b * bm + c * cm
    return grams/aam
print(molesPerKilo(7.89, 12.01, 9, 1.008, 8, 16.00, 4))
# %%
def loopDeDo(project, depend):
    order = []
    for p in project:
        for d in depend:
            if p == d[1]:
                count = 0
                for x in order:
                    count += 1
                    if x == d[0]:
                        break
                    elif x != d[0] and count == len(order):
                        try:
                            order.append(loopDeDo(project, depend))
                        except RecursionError:
                            return order, 'please debug', 'recurse to much'
        order.append(p) 
    return order
# def Projects(project, depend):
    # betde = {}
    # order = []
    # for x in project:
    #     betde[x] = []
    # for p in project:
    #     for x in depend:
    #         if x[1] == p:
    #             betde[p].append(x[0])
    # while True:
    #     try:
    #         if len(order) >= len(project):
    #             break
    #         for x in betde:
    #             if betde[x] == []:
    #                 for y in betde:
    #                     for z in betde[y]:
    #                         if z == x:
    #                             betde[y].remove(z)
    #                             break
    #                 order.append(x)
    #                 betde.pop(x)
    #     except RecursionError:
    #         return "I Quit."
    # return order
# Below is what I'm working on.
    # for x in project:
    #     for y in depend:
    #         if y[1] == x:
    #             for z in depend:
    #                 if z[1] == y[0]:
    # return None
sam = loopDeDo(['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')])
print(sam)
# %%
from statistics import mean
from math import floor
from math import ceil
def EggDrop(act):
    if act > 100 or act < 1:
        return 'egg unbreakable'
    num = 50
    minBreak = None
    first = True
    drops = 0
    while True:
        drops += 1
        if drops >= 100:
            return 'We cant do this'
            break
        if minBreak != None:
            if num >= minBreak:
                print('Funtion Bug. :(')
                break
        if num >= act:
            minBreak = num
            if num == 1:
                return 1
            if first == True:
                num == 25
            else:
                num = ceil(num/2)
        if num < act:
            if num == minBreak-1:
                break
            if first == True:
                num = 75
            else:
                if minBreak == None:
                    num = floor(num + (num/2))
                else:
                    num = floor(mean([num, minBreak]))
        first = False
    return minBreak
well = EggDrop(50)
print(well)
# %%
# This is the solution to problem 7.2, where I'm asked to simulate a call center; I deviated from the request to a model a thought made sense.  
# The input feutures a list of booleans of if a worker is occupied
# styled like so: [Director,[[Manager1,[Caller1, Caller2, Caller3]],[Manager2,[Caller1, Caller2, Caller3]]]] and so on and so fourth.
def MyModelOfDispatched(PhoneComp):
    for x in PhoneComp[2]:
        for y in x[2]:
            if y == False:
                return 'Call given'
            if y == x[2][-1]:
                if x[1] == False:
                    return 'Call given'
        if x == PhoneComp[2][-1]:
            if PhoneComp[1] == False:
                return 'Call given'
    return 'The phone company is at max capatity. You are on hold.'
def TheirModelOfDispatched(PhoneComp):
    for x in PhoneComp[2]:
        for y in x[2]:
            if y == False:
                return 'Call given'
            if y == x[2][-1]:
                if x[1] == False:
                    return 'Call given'
                elif PhoneComp[1] == False:
                    return 'Call given'
                else:
                    return 'we cant help you'
    return 'The fact that you are seeing this is a Bug'
