data = open('7').read().split('\n')
data = [i.split(':') for i in data]

nums = []
for a,b in data:
    a = [int(a)]
    b = [int(i) for i in b.split()]
    nums.append(a+b)

def solve1(m:int,n:int,x:list):
    if len(x) == 0:
        return m if m == n else 0
    nn = x[0]
    r1 = solve1(m,nn+n,x[1:])
    r2 = solve1(m,nn*n,x[1:])
    return r1+r2

def solve2(m:int,n:int,x:list):
    if len(x) == 0:
        return m if m == n else 0
    nn = x[0]
    r1 = solve2(m,nn+n,x[1:])
    r2 = solve2(m,nn*n,x[1:])
    r3 = solve2(m,int(str(n)+str(nn)),x[1:])
    return r1+r2+r3

p1 = p2 = 0
for l in nums:
    m = l[0]
    n = l[1] 
    x = l[2:]
    p1 += m if (solve1(m,n,x)) > 0 else 0
    p2 += m if (solve2(m,n,x)) > 0 else 0

print(p1)
print(p2)