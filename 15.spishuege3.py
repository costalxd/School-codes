for A in range(1,1000):
    f=0
    for x in range(1,1000):
        if ( (A<50) and ( (x%A!=0) <= ((x%10==0) <= (x%12!=0)) ) ) == 0:
            f=1
            break
    if f==0:
        print(A)