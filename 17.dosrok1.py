A=[]
f=open("17_7596.txt")
for s in f:
    A.append(int(s))
f.close()
count=0
mintr=100000
for j in range(len(A)):
    if A[j]%10==5 and len(str(A[j]))==3:
        mintr=min(mintr, A[j])
minsum=100000
for i in range(len(A)-1):
    if ( ((len(str(A[i]))==3 and len(str(A[i+1]))!=3) or (len(str(A[i]))!=3 and len(str(A[i+1]))==3)) and ((A[i]+A[i+1])%mintr==0) ):
        count+=1
        minsum=min(minsum, (A[i]+A[i+1]))
print(count, minsum)