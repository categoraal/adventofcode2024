import re
from decimal import Decimal
data = open('13').read().strip().split('\n\n')

t = 10000000000000
p1 = p2 = 0
for i,v in enumerate(data):
    n = [int(i) for i in re.findall(r'\d+',v)]
    x1,y1,x2,y2,x,y = n
    for i in range(100):
        for j in range(100):
            if x1*i+x2*j == x and y1*i+y2*j == y:
                p1 += 3*i+j
    
    x += t
    y += t
    d = Decimal(x1*y2-x2*y1)
    i = Decimal((y2*x-x2*y)*(1/d))
    j = Decimal((-y1*x+x1*y)*(1/d))
    if i%1 == 0.0 and j%1 == 0.0:
        if int(i)*x1+int(j)*x2 == x:
            p2 += 3*i+j
    elif i%1 < 0.999:
        i = int(str(i).split('.')[0])
        j = int(str(j).split('.')[0])
        if i*x1+j*x2 == x:
            p2 += 3*i+j
    elif i%1 > 0.001:
        i = int(str(i).split('.')[0])+1
        j = int(str(j).split('.')[0])+1
        if i*x1+j*x2 == x:
            p2 += 3*i+j

print(p1)
print(int(p2))
