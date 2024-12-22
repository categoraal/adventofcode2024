data = [int(i) for i in open('22').read().strip().split('\n')]

def evolve(x):
    x = ((x*64)^x)%16777216
    x = ((x>>5)^x)%16777216
    x = ((x*2048)^x)%16777216
    return x

p1 = 0
allprices = {}
for i,n in enumerate(data):
    prices = {}
    p=[]
    dif = []
    for _ in range(2000):
        p.append(int(str(n)[-1]))
        if len(p) > 1: dif.append(p[-1]-p[-2])
        if len(dif) > 3:
            key = tuple(dif[-4:])
            if key not in prices:
                prices[key] = int(str(n)[-1])#p[-1]
                if key in allprices:allprices[key] += int(str(n)[-1])
                else:allprices[key] = int(str(n)[-1])
        n = evolve(n)
    p1 += n

p2 = 0
for i in allprices:
    if allprices[i] > p2: p2 = allprices[i]

print(p1,p2,sep='\n')