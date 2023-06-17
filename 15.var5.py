s=[]
for a1 in range(1,101):
    for a2 in range(1,101):
        f=True
        for x in range(1,101):
            if not( (not(( (10 <= x <= 15) or (20 <= x <= 27) <= (a1 <= x <= a2)))) == 0):
                f=False
                break
        if f==True:
            s.append(a2-a1)
print(min(s))
#isnt working