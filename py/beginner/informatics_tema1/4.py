x=0
for i in range(1, 20, 2):
    if i%4==1: 
        x=x+(4/i)
    else:
        x=x-(4/i)
print(x)