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
