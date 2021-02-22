a=set()
x=list(map(int,input().split()))
for i in range(len(x)):
    if x[i]>0:
        a.add(x[i])
a=sorted(a)
print(a[0])