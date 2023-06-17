with open("24var09-13.txt") as f:
    s = f.readline()
    res = 0
    buf = 0
    k = 0
    for i in s:
        if i == 'Z':
            k += 1
        if k == 2:
            res = max(res, buf)
            k = 0
            buf = 0
        buf += 1
print(res)