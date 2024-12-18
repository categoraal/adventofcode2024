data = open('18').read().strip().split('\n')

data = [tuple([int(i) for i in line.split(',')]) for line in data]
bounds = set(data[0:1024])
end = (70,70)

ds = ((1,0),(-1,0),(0,1),(0,-1))
            
def solve(bounds):
    queue = [(0,0,0)]
    seen = set()
    distmap = {(0,0):1}
    while queue:
        c,r,t = queue.pop(0)
        if (c,r) == end:
            return(t)
        for dc,dr in ds:
            nc,nr = c+dc,r+dr
            if (nc,nr) not in seen and (nc,nr) not in bounds and 0 <= nc < 71 and 0 <= nr < 71:
                queue.append((nc,nr,t+1))
                distmap[(c,r)] = t+1
                seen.add((nc,nr))
    return -1

print(solve(bounds))

i = 1024
while i < len(data):
    bounds = set(data[0:i])
    if solve(bounds) == -1:
        print(','.join([str(k) for k in data[i-1]]))
        break
    i += 1