from fnmatch import *
for i in range(0, 10**8, 37):
    if fnmatch(str(i), "2*1234?6"):
        print(i, i//37)