x="0123456789ABCDE"
for i in x:
    a=int("97968"+i+"13", 15)
    b=int("7"+i+"213", 15)
    c=a+b
    if c%14==0:
        print(c//14, i)