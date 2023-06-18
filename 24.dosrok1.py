f=open("24_7600.txt")
f=f.readline()
f=f.replace("QQ", "1")
f = f.replace("QR", "1")
f = f.replace("QS", "1")
f = f.replace("RR", "1")
f = f.replace("RQ", "1")
f = f.replace("RS", "1")
f = f.replace("SS", "1")
f = f.replace("SR", "1")
f = f.replace("SQ", "1")
f=f.split("1")
maxdl=0
for i in f:
    maxdl=max(maxdl, len(i))
    if len(i)==542:
        print(i)
print(maxdl+2) #ПРОВЕРИТЬ ФАЙЛ ОБЯЗАТЕЛЬНО НАДО