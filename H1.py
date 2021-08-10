def meadian(Alist):
    check_list = type(Alist) is list 
    if check_list != True:
        return 'list only'
    val = 0
    for x in Alist:
        val += 1
    VAL = val/2
    if VAL.is_integer() == False:
        Alist.sort()
        VAL = int(VAL)
        return Alist[VAL]
    if VAL.is_integer() == True:
        Alist.sort()
        val0 = VAL-1
        val0 = int(val0)
        print(type(val0))
        return Alist[VAL]
    return None 
print(meadian([2, 1, 3, 4])) 