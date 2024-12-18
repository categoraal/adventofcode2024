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

def solve(data):
    i = len(data)-1
    bounds = set(data[:i+1])
    seen = set()
    distmap = {(0,0):1}
    queue = [(0,0,0)]
    while i > 0:   
        bounds.remove(data[i])
        bc,br = data[i]
        for dc,dr in ds:
            nbc,nbr = bc+dc,br+dr
            if (nbc,nbr) in seen:
                queue = [(bc,br,0)]
                seen.add((bc,br))
        while queue:
            c,r,t = queue.pop(0)
            if (c,r) == end:
                return(data[i])
            for dc,dr in ds:
                nc,nr = c+dc,r+dr
                if (nc,nr) not in distmap and (nc,nr) not in bounds and 0 <= nc < 71 and 0 <= nr < 71:
                    queue.append((nc,nr,t+1))
                    distmap[(c,r)] = t+1
                    seen.add((nc,nr))
        i -= 1

print(solve(data))
