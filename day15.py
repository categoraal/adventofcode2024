grid, instructions = [i.split('\n') for i in open('15').read().split('\n\n')]

kaart = {}
for r,line in enumerate(grid):
    for c,v in enumerate(line):
        kaart[(r,c)] = v
        if v == '@':
            start = (r,c)

ins = ''.join([i for i in instructions])
dirs = {'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}

def move(p,d):
    r,c = p
    dr,dc = d
    n = kaart[(r,c)] 
    queue = [p]
    cnt = 0
    for r,c in queue:
        if kaart[(r,c)] == '#':break
        nr,nc = r+dr,c+dc
        if (nr,nc) in kaart and kaart[(nr,nc)] == 'O':
            cnt += 1
            queue.append((nr,nc))
        elif kaart[(nr,nc)] == '.':
            queue.append((nr,nc))
            break
    
    f = True
    for i in queue[::-1]:
        if cnt > 0:
            kaart[i] = 'O'    
            cnt -= 1
        elif cnt == 0 and f:
            kaart[i] = '@'
            result = i
            f = False
        else:
            kaart[i] = '.' 
    return result

def draw(x):
    l = ''
    for r in range(len(grid)):
        for c in range(2*len(grid[0])):
            if (r,c) in x:
                l += x[(r,c)]
        l += '\n' 
    print(l)

p = start
for i in ins:
    p = move(p,dirs[i])    
p1 = 0
for i in kaart:
    if kaart[i] == 'O':
       r,c = i
       p1 += 100*r+c

print(p1)

#part 2
kaart = {}
for r,line in enumerate(grid):
    for c,v in enumerate(line):
        if v == '#':
            kaart[(r,2*c)] = '#'
            kaart[(r,2*c+1)] = '#'
        if v == 'O':    
            kaart[(r,2*c)] = '['
            kaart[(r,2*c+1)] = ']'
        if v == '.':
            kaart[(r,2*c)] = '.'
            kaart[(r,2*c+1)] = '.'
        if v == '@':
            start = (r,2*c)
            kaart[(r,2*c)] = '@'
            kaart[(r,2*c+1)] = '.'

def movelr(p,d):
    r,c = p
    dr,dc = d
    n = kaart[(r,c)] 
    queue = [p]
    cnt = 0
    for r,c in queue:
        if kaart[(r,c)] == '#':break
        nr,nc = r+dr,c+dc
        if (nr,nc) in kaart and kaart[(nr,nc)] in '[]':
            cnt += 1
            queue.append((nr,nc))
        elif kaart[(nr,nc)] == '.':
            queue.append((nr,nc))
            break
        else:
            return p
    
    f = True
    for i in queue[::-1]:
        if cnt > 0:
            r,c = i
            nr,nc = r-dr,c-dc
            kaart[i] = kaart[(nr,nc)]
            cnt -= 1
        elif cnt == 0 and f:
            kaart[i] = '@'
            result = i
            f = False
        else:
            kaart[i] = '.' 
    return result

def moveud(p,d):
    dr,dc = d
    queue = [p]
    nd = {}
    for r,c in queue:
        if kaart[(r,c)] == '#':
            return p
        nr,nc = r+dr,c+dc
        nd[(nr,nc)] = kaart[(r,c)]
        n = kaart[(nr,nc)]
        if n == '#':
            return p
        if n in '[]':
            queue.append((nr,nc))
            if n == '[':
                queue.append((nr,nc+1))
            else:
                queue.append((nr,nc-1))
    for i in queue:
        kaart[i] = '.'
    for i in nd:
        kaart[i] = nd[i]
    r,c = p
    return (r+dr,c+dc)
p = start
for i in ins:
    if i in '<>':
        p = movelr(p,dirs[i])    
    else:
        p = moveud(p,dirs[i])

p2 = 0
for i in kaart:
    n = kaart[i]
    if n == '[':
        r,c = i
        p2 += 100*r+c

print(p2)