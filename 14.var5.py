s=5**2022 - 2*5**1010 + 25**850 + 2500
count=0
while s>0:
    if s%5==4:
        count+=1
    s=s//5
print(count)