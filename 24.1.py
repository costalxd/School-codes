f = open('06-24.txt')
n=f.read()
n=n.replace("YX", "y")
n=n.replace("XY", "y")
n=n.replace("XZ", "y")
n=n.replace("ZX", "y")
n=n.replace("YZ", "y")
n=n.replace("ZY", "y")
n=n.replace("XX", "y")
n=n.replace("YY", "y")
n=n.replace("ZZ", "y")
k=0
m=0
for i in range(len(n)):
    if n[i]!="y":
        k+=2
        m=max(m,k)
    else:
        k=0
print(m)