from itertools import product
a = product('0123', repeat=3)
count = 0
for i in a:
    s = ''.join(i)
    if s[0] >= s[1] >= s[2] and s!="000":
        count += 1
        print(s)
print(count)