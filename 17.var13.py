A=[]
f=open("17var13.txt")
for s in f:
    A.append(int(s))
f.close()
count=0
m=-10000
for i in range(len(A)-1):
    if A[i]+A[i+1]>=100 and (A[i]<0 or A[i+1]<0):
        count+=1
        summ=A[i]*A[i+1]
        m=max(m, summ)
print(count,m)