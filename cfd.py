import numpy as np
x1=[] #water level after 24hrs
x2=[] #present waterlevel in metres
x3=[] #present discharge in cubic metres per second

with open('data.txt') as f:
    for line in f:
        data = line.split()
        x2.append(float(data[0]))
        x3.append(float(data[1]))
        x1.append(float(data[2]))

p1=sum(x1)
q1=sum(x2)
r1=sum(x3)
p2=0;p3=0;q2=0;r2=0;r3=0
for i in range(len(x1)):
    p2=p2+(x1[i]*x2[i])
    q2=q2+(x2[i]*x2[i])
    r2=r2+(x2[i]*x3[i])
    p3=p3+(x1[i]*x3[i])
    r3=r3+(x3[i]*x3[i])
X=[[p1],[p2],[p3]];
Y=np.matrix([[len(x1),q1,r1],[q1,q2,r2],[r1,r2,r3]])
B=Y.I
p=B*X
a=p[0]
b=p[1]
c=p[2]
#for i in range(len(x1)):
  # print (a+(b*x2[i])+(c*x3[i]))
g=input("enter the water level")
h=input("enter the discharge")
g=float(g)
h=float(h)
f=a+(b*g)+(c*h) #x1=a+(b*x2)+(c*x3)
if 83.5<f<85 :
    print("50%chances of flood");
elif f>85 :
    print("70-80% chances of flood");
else :
    print("no chance of flood");5
