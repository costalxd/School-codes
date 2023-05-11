s=550000
count=1
for ch in range(s+1, s+100000):
    for i in range(2,1000):
        if ch%i==0 and (ch%(i+1)==0 or ch%(i+2)==0 or ch%(i+3)==0 or ch%(i+4)==0 or ch%(i+5)==0 or ch%(i+6)==0 or ch%(i+7)==0) and count<=6:
            count+=1
            print(ch, ch//i)
            break