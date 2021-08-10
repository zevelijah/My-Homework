import math as m
def PValZ(hNull, samp, suc):
    pHat = suc/samp
    pValZ = (pHat-hNull)/m.sqrt((hNull*(1-hNull))/samp)
    return pValZ
def mode(list):
    mode_map = {}
    for num in list:
        mode_map.setdefault(num, 0)
        mode_map[num] += 1
    sorted_mode_map = sorted(mode_map.items(), key=lambda kv: kv[1], reverse=True)
    answer = []
    #sorted_mode_map[0]
    answer.append(sorted_mode_map[0])
    for pair in sorted_mode_map[1:]:
        if answer[0][1] == pair[1]:
            answer.append(pair)
        else:
            break
    return answer
list = [2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 2]
mode(list)
import math as m
import scipy.stats as st
def Cantthinkofname(co, s1, a1, s2, a2):
    x1 = (s1/a1)
    x2 = (s2/a2) 
    y = (s1/a1) - (s2/a2)
    pValrR = (1 - co)/2
    z = st.norm.ppf(pValrR)
    posa = y + (z * (m.sqrt(((x2*(1-x2))/a2) + (x1*(1-x1))/a1)))
    nega = y - (z * (m.sqrt(((x2*(1-x2))/a2) + (x1*(1-x1))/a1)))
    return posa, nega, y, (z * (m.sqrt(((x2*(1-x2))/a2) + (x1*(1-x1))/a1))), z, s1/a1, s2/a2
print(Cantthinkofname(0.99, 80, 400, 150, 600))
import math as m
import scipy.stats as st
def Cantthinkofname1(s1, a1, s2, a2):
    x1 = (s1/a1)
    x2 = (s2/a2) 
    y = (s1/a1) - (s2/a2)
    pc = (s1 + s2)/(a1 + a2)
    z = y/m.sqrt((((pc*(1-pc))/a2) + (pc*(1-pc))/a1))
    pval = 1 - st.norm.cdf(z)
    return pval, pval*2
print(Cantthinkofname1(30, 50, 20, 50))  
from math import sqrt as s
def thing(n1, s1, a1, n2, s2, a2):
    t = (a1-a2)/(s(((s1**2)/n1)+((s2**2)/n2)))
    return t
print(thing(104, 67, 9, 112, 8, 70))
def Meadian(Alist):
    check_list = type(Alist) is list 
    if check_list != True:
        return 'list only'
    val = 0
    for x in Alist:
        val += 1
    VAL = val/2
    if VAL.is_integer():
        Alist.sort()
        VAL = int(VAL)
        vin = VAL-1
        vin = int(vin)
        return Alist[vin], Alist[VAL]
    else:
        Alist.sort()
        VAL = int(VAL)
        return Alist[VAL]
    return "Funny, Your not suposed to see this unless your computer breaks. error infinity."
  