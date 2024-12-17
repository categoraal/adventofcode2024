import heapq
data = open('16').read().split('\n')

grid = {}

for r,l in enumerate(data):
    for c,v in enumerate(l):
        grid[(r,c)] = v
        if v == 'S':
            start = (r,c)
        if v == 'E':
            end = (r,c)

print(start,end)

pq = [(0,start,(0,1),[start])]

dirs = ((1,0),(-1,0),(0,1),(0,-1))
seen = {}
lowest_cost = 1E20
path = set()
while True:
    cost,p,d,subpath = heapq.heappop(pq)
    seen[(p,d)] = cost
    r,c = p
    if p == end:
        if cost < lowest_cost:
            lowest_cost = cost
            path = set(subpath)
        elif cost == lowest_cost:
            path |= set(subpath)
        else: 
            break
    
    for dr,dc in dirs:
        nd = (dr,dc)
        nr,nc = r+dr,c+dc
        n = grid[(nr,nc)]
        if n == '#' or d == (-dr,-dc):continue
        new_cost = cost + 1 if (dr,dc) == d else cost + 1001
        if ((nr,nc),nd) in seen:continue
        heapq.heappush(pq,(new_cost,(nr,nc),nd,subpath+[(nr,nc)]))

print(lowest_cost)
print(len(path))