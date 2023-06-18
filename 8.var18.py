from itertools import product
a=product("ABC", repeat=6)
count=0
for i in a:
    s="".join(i)
    if s.count("A")==1:
        count+=1
print(count)