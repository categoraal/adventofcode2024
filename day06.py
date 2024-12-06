import time
a = time.time()
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
print(time.time()-a)
p2 = 0
k2 = {} 
 
for p in list(visited):
    dc,dc = (-1,0)
    if kaart[p] in '^#':continue
    kaart[p] = '#' 
    seen = set()
    seen.add(start)
    p2 += (path(p1=False))
    kaart[p] = '.'

print(p2) 
print(time.time()-a)
