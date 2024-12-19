colors,designs= open('19').read().strip().split('\n\n')

colors = colors.split(', ')
designs = designs.split('\n')

cache = {}
def solve(x):
    r = 0
    if x in cache:
        return cache[x]    
    for c in colors:
        if c == x:
            r += 1
        if x.startswith(c):
            l = len(c)
            r += solve(x[l:])
    cache[x] = r
    return r
p1 = p2= 0

reducedcolors = reduce(colors)
for design in designs:
    # p1 += solve1(design,design,reducedcolors)
    n=solve(design)
    p2 += n
    p1 += 1 if n > 0 else 0
print(p1)
print(p2)