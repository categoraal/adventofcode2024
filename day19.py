colors,designs= open('19').read().strip().split('\n\n')

colors = colors.split(', ')
designs = designs.split('\n')

cache = {}
def solve(x):
    r = 0
    if x in cache: return cache[x]    
    for c in colors:
        if c == x: r += 1
        if x.startswith(c): r += solve(x[len(c):])
    cache[x] = r
    return r

p1 = p2= 0
for design in designs:
    n=solve(design)
    p2 += n
    p1 += 1 if n > 0 else 0
print(p1,p2,sep='\n')