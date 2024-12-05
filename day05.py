data = open('5').read().split('\n\n')

rules,pages = data

rules = rules.split('\n')
pages = [i.split(',') for i in pages.split('\n')]

rdict = {}
for line in rules:
    a,b = line.split('|')
    if a in rdict:
        rdict[a].append(b)
    else:
        rdict[a] = [b]

def checkpages(x):
    for i,v in enumerate(x):
        if v not in rdict:continue
        later = rdict[v]
        for l in later:
            if l in x:
                if x.index(l) < i:
                    return 0
    return int(x[int((len(x)-1)/2)]) 

p1 = 0
wrongpages = []
for p in pages:
    x = checkpages(p)
    p1 += x
    if x == 0:
        wrongpages.append(p)

print(p1)

def checkidx(x):
    wrongindex = []
    f = True
    while f:
        for i,v in enumerate(x):
            if v not in rdict:continue
            later = rdict[v]
            for l in later:
                if l in x:
                    if x.index(l) < i:
                        temp = x.index(l)
                        x[temp] = v
                        x[i] = l
                        r = checkpages(x)
                        if r != 0:
                            return r
                        else:
                            break

                            
    return wrongindex

p2 = 0
for p in wrongpages:
    x =checkidx(p)
    p2 += x

print(p2)