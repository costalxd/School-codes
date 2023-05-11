start=860000
count=1
for ch in range(start+1, start+100000):
    for i in range(2,1000):
        if ch%i==0:
            M=(ch//i)-i
            if M%100==18 and count<=5:
                count+=1
                print(ch, M)
            break