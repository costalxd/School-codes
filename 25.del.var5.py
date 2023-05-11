start=860000
for ch in range(start, start+100000):
    for i in range(2,1000):
        if ch%i==0:
            M=(ch//i)-i
            if M%100==18:
                print(ch, M)
            break