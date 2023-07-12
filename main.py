n= input("Enter a even digit number")
x=n.split(" ")
a=[]
for i in x:
    a.append(i.strip())
x=a
if len(x)%2==0:
    y={}
    k=()
    c=0
    for i in range (0, len(x)-1,2):
        a=(x[i], x[i+1])
        b={a:0}
        y.update(b)
    for i in range (0, len(x)-1,2):
        if (x[i], x[i+1]) in y:
            y[(x[i], x[i+1])]=y[(x[i], x[i+1])]+1
    r=max(y.values())
    for i in y:
        if r==y[i]:
            k=i
    for i in y:
        if i[0] != k[0]:
            c+=y[i]
        if i[1] != k[1]:
            c+=y[i]
    print(c)
else:
    print("Invalid Input")




