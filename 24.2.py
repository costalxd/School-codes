f = open('01-24.txt')
s = f.read()
m = 0
k = 0
i = 0
while i < len(s):
    if s[i] in 'CDF' and s[i+1] in 'AO':
        k += 1
        i += 2
        if k > m:
            m = k
    else:
        k = 0
        i += 1
print(m)