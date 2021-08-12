# Each pet is a tuple of their (name, type). Types are are all lowercase for easy cycle.
while True:
    Orphanage = [("falad", 'dog'), ('mittens', 'cat'), ('chester', 'cat')]
    print("welcome to our pet shelter")
    workOrCus = input("Are you here to\n1.get\n2.give\n")
    if workOrCus == '1':
        catOrDog = input("would you like \n1.cat\n2.Dog\n3.either\n")
        if catOrDog == '1':
            for pet in Orphanage:
                if pet[1] == 'cat':
                    print(f'Your pet is { pet }')
                    Orphanage.remove(pet)
                    break
        elif catOrDog == '2':
            for pet in Orphanage:
                if pet[1] == 'dog':
                    print(f'Your pet is { pet }')
                    break
        elif catOrDog == '3':
            for pet in Orphanage:
                print(f'Your pet is { pet }')
                break
        else:
            print('get out of my store- I mean, shelter')
            break
    elif workOrCus == '2':
        askname = input('name?\n')
        rtype = input('Type? enter in all lowercase.\n')
        if rtype != 'dog' and rtype != 'cat':
            print('we only take dogs and cats')
            break
        Orphanage.append((askname, rtype))
    else:
        print('give a strait answer')
        break
    break