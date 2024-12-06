import copy
data = open('6').read().split('\n')

kaart = {}
for r,v in enumerate(data):
    for c,v2 in enumerate(v):
        kaart[(r,c)] = v2
        if v2 == '^':
            start = (r,c) 

seen = set()
seen.add(start)

queue = [(*start,-1,0)]
dc,dc = (-1,0)
ds = {(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
cnt = 0
def path(p1):
    queue = [(*start,-1,0)]
    dc,dc = (-1,0)
    ds = {(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
    for r,c,dr,nc in queue:
        if (r,c,dr,nc) in seen: return 1 
        if p1:seen.add((r,c))
        else:seen.add((r,c,dr,dc))

        nr,nc = r+dr,c+dc
        if (nr,nc) not in kaart:
            if p1:print(len(seen));return seen
            else:return 0
        elif kaart[(nr,nc)] =='#':
            dr,dc = ds[(dr,dc)]
            queue.append((r,c,dr,dc))
        else:
            queue.append((nr,nc,dr,dc))

        
visited = path(p1=True)
    
p2 = 0
pos = list(kaart.keys())
k2 = {} 
for r,v in enumerate(data):
    for c,v2 in enumerate(v):
        k2[(r,c)] = v2
 
for p in list(visited):
    dc,dc = (-1,0)
    kaart = copy.copy(k2)
    if kaart[p] in '^#':continue
    kaart[p] = '#' 
    seen = set()
    seen.add(start)
    queue = [(*start,-1,0)]
    p2 += (path(p1=False))

print(p2) 