for A in range(1, 1000):
    f=0
    for x in range(0,1000):
        for y in range(0,1000):
            if ( (x<A) and (y<A) and (x*y>1200) ) == 0:
                f+=1
            if f==1000*1000:
                print(A)

