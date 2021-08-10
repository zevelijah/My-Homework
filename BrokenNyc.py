# %%
# NY Times SPELlING BEE TM break ;)
import enchant as en
from itertools import combinations_with_replacement as cwr
from itertools import permutations as per
# gives all UNIQUE permutions of a string
# I got it from Stack Overflow
def unique_perms(series):
    return {"".join(p) for p in per(series)}
# tuple to string
# got it from W3schools
def convertTuple(tup):
    str =  ''.join(tup)
    return str
# list to string
# got it from GeeksForGeeks
def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
    return str1 
# does most of work; takes letters as a list of strings as "daily", number of letter in answer as "num" , required letter as "re" 
# daily includes required letter too; that is, re
def GrandmaWordGame(daily, num, re): 
    # makes sure that daily is list
    check_list = type(daily) is list 
    if check_list != True:
        return ' input can be List only'
    # sets a variable to the english dictionary that lets spellcheck with it
    Diction = en.Dict("en_US")
    words_2_fakes = list(cwr(daily, num))  # list of tuples showing differnt combos of daily at set legnth, legnth "num", an input 
    n_fake_words = [] 
    for fake_2_word in words_2_fakes:
        fake_word = convertTuple(fake_2_word)
        n_fake_words.append(fake_word)
    fake_words = []
    for fake_word in n_fake_words:
        x = sorted(unique_perms(fake_word))
        fake_words.append(x)
    words = []
    for fake_word_l in fake_words:
        for fake_word in fake_word_l:
            what = Diction.check(fake_word)
            if what == True:
                words.append(fake_word)
    final = []
    for word in words:
        for let in word:
            if let == re:
                final.append(word)
                break
    return final
def idea(daily, re):
    nm = 3
    ans = []
    while True:
        nm += 1
        w = GrandmaWordGame(daily, nm, re)
        ans.append(w)
        if nm == 8:
            break
    return ans
print(idea(['t', 'm', 'e', 'c', 'l', 'i', 'n'], 'l'))
# %%
