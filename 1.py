array=[]
n=int(input())
x=0
for i in range(n):
    a=float(input())
    array.append(a)
    x=x+a
A=x/n #средняя арефметическая 
y=0
for i in array:
    y=y+((A-i)**2)
D=y/(n-1) #стандартные (среднеквадратические) отклонения
print(D**(1/2))
