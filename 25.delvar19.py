s=550000
count=1
def prostoe(n):
    for x in range(2, n):
        if n%x==0:
            return False
    return True
for ch in range(s+1, s+100000):
    summ=0
    for i in range(2, ch):
       if ch%i==0 and prostoe(i):
           summ+=i
    if summ%10==1:
        print(ch, summ)
