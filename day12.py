data = open('12').read().strip().split('\n')

kaart = {}
for r,line in enumerate(data):
    for c, v in enumerate(line):
        kaart[(r,c)] = v

seen = set()
dirs = ((1,0),(-1,0),(0,-1),(0,1))

def solve(x):
    key = kaart[x] 
    queue = [x]
    perimeter = set()
    vis = set()
    for r,c in queue:
        vis.add((r,c))
        for dr,dc in dirs:
            nr,nc = r+dr,c+dc
            if (nr,nc) in kaart and (nr,nc) not in vis and kaart[(nr,nc)] == key: 
                seen.add((nr,nc))
                vis.add((nr,nc))
                queue.append((nr,nc))
            else:
                if (nr,nc) in vis: continue
                perimeter.add((nr,nc,dr,dc))
    return queue,perimeter

def findperimeter(x):
    vis = set() 
    cnt = 0 
    for i in x:
        if i in vis: continue
        cnt += 1
        r,c,ddr,ddc = i     
        queue = [(r,c)]
        vis.add((r,c,ddr,ddc))
        for r,c in queue:
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (nr,nc,ddr,ddc) in x and (nr,nc,ddr,ddc) not in vis: 
                    queue.append((nr,nc))
                    vis.add((nr,nc,ddr,ddc))
    return cnt

p1 = 0
p2 = 0
for i,x in enumerate(kaart):
    r,c = x
    if (r,c) in seen: continue
    reg,per = solve((r,c))
    p1 += len(reg)*len(per)
    fences = findperimeter(per)
    p2 += len(reg)*fences

print(p1)
print(p2)