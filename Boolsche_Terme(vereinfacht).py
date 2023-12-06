def term_1(a, b):
    return not a and not b

def term_2(a, b, c):
    return (a and c) or (b and not c)

def term_3():
    return False

def term_4(a, b, c):
    return a or (not b and not c)




