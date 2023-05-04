for x in '0123456789ABCDE':
    t=int('97968' + x + '13', 15) + int('7' + x + '233', 15)
    if t%14 == 0:
        print(t//14, x)