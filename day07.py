data = open('7').read().split('\n')
data = [i.split(':') for i in data]

nums = []
for a,b in data:
    a = [int(a)]
    b = [int(i) for i in b.split()]
    nums.append(a+b)

p1 = 0
for l in nums:
    tomatch = l[0]
    r = [l[1]]
    for i in l[2:]:
        r2 = [[k*i,k+i] for k in r]
        r= [x for xs in r2 for x in xs] 
    if tomatch in r:
        p1 += tomatch

print(p1)

p2 = 0
for l in nums:
    tomatch = l[0]
    r = [l[1]]
    for i in l[2:]:
        r2 = [[k*i,k+i,int(str(k)+str(i))] for k in r]
        r= [x for xs in r2 for x in xs] 
    if tomatch in r:
        p2 += tomatch

print(p2)   