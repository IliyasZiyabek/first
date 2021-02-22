x=list(map(int,input().split()))
for i in range(len(x)):
    if x[i]==0:
        x.remove(i) and x.add(0)
for i in range(len(x)):
    print(x[i], end=" ")