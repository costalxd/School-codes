def prost(n):
    for x in range(2, n):
        if n%x == 0:
            return False
    return True
def prdl(n): #проверка делителей
    A = 0
    for x in range(2, n//2+1):
        if n%x == 0 and prost(x):
            A+=x
    return A
start=550000
count=1
for ch in range(start+1, start+100001):
    sumdel=prdl(ch)
    if sumdel%10==7 and count<=5:
        count+=1
        print(ch, sumdel)