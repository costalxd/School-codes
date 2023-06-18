from itertools import product
a=product("0123456789", repeat=4)
count=0
for i in a:
    s="".join(i)
    if s[0]==s[1] and s[2]!=s[3] and s[0]!="0":
        if s.count(s[0])==2:
            count+=1
    if s[1]==s[2] and s[0]!=s[3] and s[0]!="0":
        if s.count(s[1])==2:
            count+=1
    if s[2]==s[3] and s[0]!=s[1] and s[0]!="0":
        if s.count(s[2])==2:
            count+=1
print(count)