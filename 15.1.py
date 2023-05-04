for A in range(0,500):
    for x in range(0,500):
        flag=1
        if ( (x & 39)==0 or (((x & 11)==0) <= ((x & A)!=0)) ) == False:
            flag=0
            break
    if flag==1:
        print(A)
        break