x=list(map(int,input().split()))
x.sort(reverse=True)
for i in range(len(x)):
    print(x[i], end=" ")