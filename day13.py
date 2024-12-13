data = open('13').read().strip().split('\n\n')

t = 10000000000000
p1 = p2 = 0
def solve(x1,y1,x2,y2,x,y):
    d = (x1*y2-x2*y1)
    i = ((y2*x-x2*y)/d)
    j = ((-y1*x+x1*y)/d)
    for n in [-1,0,1]:
        if (int(i)+n)*x1+(int(j)+n)*x2 == x and (int(i)+n)*y1+(int(j)+n)*y2 == y:
            return (int(i)+n)*3+(int(j)+n)
    return 0

for v in data:
    x1,y1,x2,y2,x,y = [x for xss in [[int(''.join([f for f in j if f.isnumeric()])) for j in k.split(',')] for k in v.split('\n')] for x in xss]
    # p1 += (sum([x for xss in [[3*i+j for i in range(100) if x1*i+x2*j == x and y1*i+y2*j == y] for j in range(100)] for x in xss]))
    p1 += solve(x1,y1,x2,y2,x,y)
    p2 += solve(x1,y1,x2,y2,x+t,y+t)

print(p1)
print(p2)