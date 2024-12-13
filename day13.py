data = open('13').read().strip().split('\n\n')

t = 10000000000000
p1 = p2 = 0
for i,v in enumerate(data):
    n = [x for xss in [[int(''.join([f for f in j if f.isnumeric()])) for j in k.split(',')] for k in v.split('\n')] for x in xss]
    x1,y1,x2,y2,x,y = n 
    for i in range(100):
        for j in range(100):
            if x1*i+x2*j == x and y1*i+y2*j == y:
                p1 += 3*i+j
    
    x += t
    y += t
    d = (x1*y2-x2*y1)
    i = ((y2*x-x2*y)/d)
    j = ((-y1*x+x1*y)/d)
    for n in [-1,0,1]:
        if (int(i)+n)*x1+(int(j)+n)*x2 == x and (int(i)+n)*y1+(int(j)+n)*y2 == y:
            p2 += (int(i)+n)*3+(int(j)+n)

print(p1)
print(p2)