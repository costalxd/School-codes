from itertools import product
a=product("01234567", repeat=5)
count=0
for i in a:
    s="".join(i)
    if s[0]=="4" and s[1]=="4" and int(s[2])%2==0 and s[2]!="4" and s[3]!="4" and s[4]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[0]=="4" and s[2]=="4" and int(s[1])%2==0 and int(s[3])%2==0 and s[1]!="4" and s[3]!="4" and s[4]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[0]=="4" and s[3]=="4" and int(s[1])%2==0 and int(s[2])%2==0 and int(s[4])%2==0 and s[1]!="4" and s[2]!="4" and s[4]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[0]=="4" and s[4]=="4" and int(s[1])%2==0 and int(s[3])%2==0 and s[1]!="4" and s[2]!="4" and s[3]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[1]=="4" and s[2]=="4" and int(s[0])%2==0 and int(s[3])%2==0 and s[0]!="4" and s[3]!="4" and s[4]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[1]=="4" and s[3]=="4" and int(s[0])%2==0 and int(s[2])%2==0 and int(s[4])%2==0 and s[0]!="4" and s[2]!="4" and s[4]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[1]=="4" and s[4]=="4" and int(s[0])%2==0 and int(s[2])%2==0 and int(s[3])%2==0 and s[0]!="4" and s[2]!="4" and s[3]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[2]=="4" and s[3]=="4" and int(s[1])%2==0 and int(s[4])%2==0 and s[0]!="4" and s[1]!="4" and s[4]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[2]=="4" and s[4]=="4" and int(s[1])%2==0 and int(s[3])%2==0 and s[0]!="4" and s[1]!="4" and s[3]!="4" and s[0]!="0":
        count+=1
        print(s)
    if s[3]=="4" and s[4]=="4" and int(s[2])%2==0 and s[0]!="4" and s[1]!="4" and s[2]!="4" and s[0]!="0":
        count+=1
        print(s)
print(count)