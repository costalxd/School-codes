s="2"+31*"5"
while "25" in s or "355" in s or "555" in s:
    s=s.replace("25", "5", 1)
    s=s.replace("355", "25", 1)
    s=s.replace("555", "3", 1)
print(s)
