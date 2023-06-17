from functools import lru_cache
import sys

sys.setrecursionlimit(2000)
@lru_cache
def f(n):
    if n==1:
        return 1
    if n>1:
        return n*f(n-1)
print(f(446)//f(443))

