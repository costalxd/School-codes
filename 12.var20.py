import random
def prost(n):
    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1
for n in range(1, 100):
    a = list(f"{23*'1'+n*'2'+25*'3'}")
    random.shuffle(a)
    a = ''.join(a)
    a = f">{a}"
    for _ in range(10000):
        a = a.replace('>1', '1>', 1)
        a = a.replace('>2', '>3', 1)
        a = a.replace('>3', '>11', 1)
    summa = a.count('1')+a.count('2')*2+a.count('3')*3
    if prost(summa):
        print(n)
        break