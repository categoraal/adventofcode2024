import time
from multiprocessing import Pool
data = open('6').read().split('\n')

kaart = {}
for r,v in enumerate(data):
    for c,v2 in enumerate(v):
        kaart[(r,c)] = v2
        if v2 == '^':
            start = (r,c) 


cnt = 0
def path(p1,cc=(-2,-2)):
    seen = set()
    seen.add(start)

    queue = [(*start,-1,0)]
    dc,dc = (-1,0)
    ds = {(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
    for r,c,dr,nc in queue:
        if (r,c,dr,nc) in seen: return 1 
        if p1:seen.add((r,c))
        else:seen.add((r,c,dr,dc))

        nr,nc = r+dr,c+dc
        if (nr,nc) not in kaart:
            if p1:print(len(seen));return list(seen)
            else:return 0
        elif kaart[(nr,nc)] =='#' or (nr,nc)==cc:
            dr,dc = ds[(dr,dc)]
            queue.append((r,c,dr,dc))
        else:
            queue.append((nr,nc,dr,dc))
        
visited = path(p1=True)
a = time.time()
p2 = 0
def solve2(p): 
    if kaart[p] in '^#':return 0
    res = (path(p1=False,cc=p))
    return res

if __name__ == '__main__':
    with Pool(8) as p:
        p2 = sum(p.map(solve2,visited))
        print(p2)
print(time.time()-a)

