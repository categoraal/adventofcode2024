data = [i.split('-') for i in open('23').read().strip().split('\n')]

graph = {}
for a,b in data:
    if a in graph: graph[a].add(b) 
    else:graph[a] = {b}
    if b in graph: graph[b].add(a)
    else:graph[b] = {a}
    graph[a].add(a)
    graph[b].add(b)

seen = set()
for i in graph:
    for j in graph:
        if i == j:continue
        inter = graph[i]&graph[j]
        cnt = 0
        if i not in inter or j not in inter: continue
        for k in inter:
            if k == i or k == j:continue
            if i in graph[k] and j in graph[k]:
                if i[0] == 't' or j[0] == 't' or k[0] == 't':
                    seen.add(tuple(sorted([i,j,k])))
print(len(seen))

best = {}
for i in graph:
    for j in graph:
        if i == j:continue
        inter = graph[i]&graph[j]
        if len(inter)<len(best):continue
        cnt = 0
        for k in inter:
            if inter == graph[k]&inter:
                cnt += 1
        if cnt == len(inter):
            best = inter

print(','.join(sorted(list(best))))