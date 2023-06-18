for A in range(1,1000):
    f=0
    for x in range(1,1000):
        if ( (x%A!=0) <= ( (x%6==0) <= (x%4!=0)) ) == 0:
            f=1
            break
    if f==0:
        print(A)