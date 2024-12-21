import re
from functools import cache
data = open('21').read().strip().split('\n')
print(data)
keypad = {'g':-2,'7':-2+3j,'8':-1+3j,'9':3j,'4':-2+2j,'5':-1+2j,'6':2j,'1':-2+1j,'2':-1+1j,'3':1j,'0':-1,'A':0}
dpad = {'g':-2,'^':-1,'A':0,'<':-2-1j,'v':-1-1j,'>':-1j}
ddir = {'^':1j,'<':-1,'v':-1j,'>':1,'A':0}
ds = (1,-1,1j,-1j)
# def gen(x,ins):
#     buttons = ''
#     p = ins['A']
#     for l in x:
#         np = ins[l]
#         d = np-p
#         r = int(d.real);c = int(d.imag)
#         buttons += -r*'<' if r < 0 else r*'>'
#         buttons += -c*'v'+'A' if c < 0 else c*'^'+'A'
#         p = np
#     return buttons
# @cache
def gen(x,ins):
    buttons = ''
    p = ins['A']
    for l in x:
        np = ins[l]
        d = np-p
        r = int(d.real);c = int(d.imag)
        b = -r*'<' if r < 0 else r*'>'
        b += -c*'v'+'A' if c < 0 else c*'^'+'A'
        for i in b:
            p+=ddir[i]
            if p == -2:
                b = -c*'v' if c < 0 else c*'^'
                b += -r*'<'+'A' if r < 0 else r*'>'+'A'
                break
        p = np
        buttons += b
    return buttons

p1 = 0
for i in data:
    pp = gen(i,keypad)
    pp = gen(pp,dpad)
    pp = gen(pp,dpad)
    num = int(i[:-1])
    p1 += num*len(pp)

print(p1)

def manhattan(x,y): return int(abs((y-x)**2))

def solve(x,y):
    res = []
    queue = [(x,y,'')]
    while queue:
        x,y,moves = queue.pop(0)
        if x==y:
            res.append(moves+'A')
            # print(moves)
        for i in ddir:
            d = ddir[i] 
            # print('d',d)
            if manhattan(x,y)>manhattan(x+d,y):
                if x+d == -2:continue
                queue.append((x+d,y,moves+i))
                # res.append(solve(x+d,y,moves+i))
                # solve(x+d,y,moves+i)
    return res
    
def shortestpath(x):
    s1 = 'A'
    paths = ['']
    for s2 in x:
        p = solve(keypad[s1],keypad[s2])
        npaths = []
        for i in paths:
            for j in p:
                npaths.append(i+j) 
        paths = [i for i in npaths]
        s1 = s2
    res = []
    ap = [] 
    for i in paths:
        # print(len(i))
        for _ in range(2):
            i = gen(i,dpad) 
            # print(len(i))
        # print()
        res.append(len(i)*int(x[:-1]))
    # [print(i) for i in ap]
    # print('\n')
    return min(res)

p1 = 0
for i in data:
    p1 += shortestpath(i)
    # break

print(p1)

# part 2


    
#179198 too high     
# def keygen(x):
#     # print(x)
#     buttons = ''
#     p = keypad['A']
#     for l in x:
#         np = keypad[l]
#         d = np-p
#         r = int(d.real);c = int(d.imag)
#         buttons += -r*'<' if r < 0 else r*'>'
#         buttons += -c*'v'+'A' if c < 0 else c*'^'+'A'
#         p = np
#     return buttons

# def dgen(x):
#     buttons = ''
#     p = dpad['A']
#     for l in x:
#         np = dpad[l]
#         d = np-p
#         r = int(d.real);c = int(d.imag)
#         buttons += -r*'<' if r < 0 else r*'>'
#         buttons += -c*'v'+'A' if c < 0 else c*'^'+'A'
#         p = np
#     return buttons
# print(dgen(dgen(keygen(data[0]))))

# pp = dgen(dgen(keygen(i)))