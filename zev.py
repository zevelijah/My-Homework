def factorial(x):
    m = x
    a = [x]
    while True:
        m -= 1
        if m == 0:
            break
        else:
            a.append(m)
    w = 1
    for y in a:
        w *= y
    return w