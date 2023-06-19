for A in range(0,1000):
    f=0
    for x in range(0,1000):
        for y in range(0,1000):
            if ( (x>=A) or (y>=A) or ((x*y) <= 200) ) == 0:
                f=1
                break
    if f==0:
        print(A)