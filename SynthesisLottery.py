# %%
import random
def lottery(Cities, Teams):
    check_list1 = type(Cities) is list 
    if check_list1 != True:
        return ' input can be List only'
    check_list2 = type(Teams) is list 
    if check_list2 != True:
        return ' input can be List only'
    if len(Cities) < len(Teams):
        print('Less cities than teams. loop back manually until all teams acounted for.')
    random.shuffle(Teams)
    pairs = zip(Teams, Cities) # If less Cities than teams, unacounted teams will be looped back manually
    return tuple(pairs), Teams
# put the cities in order of poulation
lot = lottery(['Tyo, Nyc, Lax', 'Par', 'Win', 'kin'], ['mag', 'blue', 'cya', 'gold', 'red'])
print(lot)
# %%
import random
def MyOwnZip(tem, cits):
    par = []
    for x in tem:
        cit = cits[0]
        tup = (x, cit)
        
    return None
def lottery(Cities, Teams):
    check_list1 = type(Cities) is list 
    if check_list1 != True:
        return ' input can be List only'
    check_list2 = type(Teams) is list 
    if check_list2 != True:
        return ' input can be List only'
    if len(Cities) < len(Teams):
        print('Less cities than teams. loop back manually until all teams acounted for.')
    random.shuffle(Teams)
    pairs = zip(Teams, Cities) # If less Cities than teams, unacounted teams will be looped back manually
    return pairs, Teams
# put the cities in order of poulation
lot = lottery(['Tyo, Nyc, Lax', 'Par', 'Win', 'kin'], ['mag', 'blue', 'cya', 'gold', 'red'])
print(lot)