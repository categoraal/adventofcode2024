from functools import cache
colors,designs= open('19').read().strip().split('\n\n')

colors = colors.split(', ')
designs = designs.split('\n')

def solve1(i,design,colors,f=False):
    queue = [design]
    while queue:
        x = queue.pop(-1)
        for c in colors:
            if f and c == i: continue
            if c == x: return 1
            if x.startswith(c):
                l = len(c)
                queue.append((x[l:]))
    return 0

def reduce(x):
    r = []
    for i in x:
        if solve1(i,i,colors,True) == 0:
            r.append(i)
    return r

@cache
def solve2(x):
    r = 0
    for c in colors:
        if c == x:
            r += 1
        if x.startswith(c):
            l = len(c)
            r += solve2(x[l:])
    return r

p1 = p2= 0

reducedcolors = reduce(colors)
for design in designs:
    p1 += solve1(design,design,reducedcolors)
    p2 += solve2(design)
print(p1)
print(p2)
