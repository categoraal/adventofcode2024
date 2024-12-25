from itertools import pairwise
data = open('21').read().strip().split('\n')

keypad = {'g':-2,'7':-2+3j,'8':-1+3j,'9':3j,'4':-2+2j,'5':-1+2j,'6':2j,'1':-2+1j,'2':-1+1j,'3':1j,'0':-1,'A':0}
dpad = {'^':-1,'A':0,'<':-2-1j,'v':-1-1j,'>':-1j} #'g':-2,
ddir = {'^':1j,'<':-1,'v':-1j,'>':1,'A':0}
ds = (1,-1,1j,-1j)

def genmoves(x,y):
    d = dpad[y]-dpad[x]
    r = int(d.real);c = int(d.imag)
    return abs(r)+abs(c)+1     

def genbeginpaths(x,y,pad):
    p1 = pad[x]
    p2 = pad[y]
    d = p2-p1
    r,c = int(d.real), int(d.imag)
    res = []
    b = -r*'<' if r < 0 else r*'>'
    b += -c*'v'+'A' if c < 0 else c*'^'+'A' 
    res.append(b)
    for i in b:
        p1 += ddir[i]
        if p1 == -2: res.remove(b)

    p1 = pad[x]   
    b = -c*'v' if c < 0 else c*'^'
    b += -r*'<'+'A' if r < 0 else r*'>'+'A'
    if b in res: return res
    res.append(b)
    for i in b:
        p1 += ddir[i]
        if p1 == -2: res.remove(b)
    return res

def genpaths(x,y,pad):
    p1 = pad[x]
    p2 = pad[y]
    d = p2-p1
    r,c = int(d.real), int(d.imag)
    res = []
    b = 'A'
    b += -r*'<' if r < 0 else r*'>'
    b += -c*'v'+'A' if c < 0 else c*'^'+'A' 
    res.append(b)
    for i in b:
        p1 += ddir[i]
        if p1 == -2: res.remove(b)

    p1 = pad[x]   
    b = 'A'
    b += -c*'v' if c < 0 else c*'^'
    b += -r*'<'+'A' if r < 0 else r*'>'+'A'
    if b in res: return res
    res.append(b)
    for i in b:
        p1 += ddir[i]
        if p1 == -2: res.remove(b)
    return res
    
def shortestpath(x):
    s1 = 'A'
    paths = ['']
    for s2 in x:
        p = genbeginpaths(s1,s2,keypad)
        npaths = []
        for i in paths:
            for j in p:
                npaths.append(i+j) 
        paths = [i for i in npaths]
        s1 = s2
    return paths

cache = {}
for i in dpad:
    for j in dpad:
        if i != j and ddir[i] + ddir[j] == 0:continue
        cache[(25,i+j)] = genmoves(i,j)

d = 24
while d >= 0:
    for i in dpad:
        for j in dpad:
            if i != j and ddir[i] + ddir[j] == 0:continue
            paths=genpaths(i,j,dpad)
            l = []
            for path in paths:            
                score = sum([cache[(d+1,''.join(k))] for k in pairwise(path)])
                l.append(score) 
            cache[(d,i+j)] = min(l)
    d -= 1

p1 = 0
p2 = 0
for i in data:
    l1 = []
    l2 = []
    for path in shortestpath(i):
        l1.append(sum([cache[(24,''.join(k))] for k in pairwise('A'+path)]))
        l2.append(sum([cache[(1,''.join(k))] for k in pairwise('A'+path)]))
    p1 += min(l1)*int(i[:-1])
    p2 += min(l2)*int(i[:-1])

print(p1)
print(p2)