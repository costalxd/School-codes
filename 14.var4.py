s=1331**650 - 55*121**610 + 77*11**510 - 3*11**100 - 221
count=0
while s>0:
    if s%11==10:
        count+=1
    s=s//11
print(count)