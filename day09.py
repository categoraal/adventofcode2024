data = open('9').read()
n = []
for i,v in enumerate(data):
    for k in range(int(v)):
        if i%2 == 1:
            n.append(' ')
        else:
            n.append(i//2)

idx = 0
ide = len(n)-1
while idx < len(n):
    p = 0
    while idx < len(n) and n[idx] != ' ':
        idx += 1
    while n[ide] == ' ':
        ide += -1
    p = n[ide]
    if idx > ide:
        break
    n[ide] = ' '
    n[idx] = p

p1 = 0
for i,v in enumerate(n):
    if v != ' ':
        p1 += i*v
    if v == ' ':
        break
print(p1)
# part 2

idx = 0
mmap = {}
keys = []
emptys = []
for i,v in enumerate(data):
    f = idx*i
    if i%2== 0: 
        keys.append(i)
        mmap[i] = int(v) * [i//2]
    else:
        emptys.append(i)
        mmap[i] = int(v)*[' ']
    idx += 1

e = 1
k = keys[-1]

for k in keys[::-1]:
    l = len(mmap[k])
    tr = []
    for i in emptys:
        if i > k:
            break
        l2 = mmap[i].count(' ')
        if l2 == 0:
            tr.append(i)
        if l <=l2:
            idx = mmap[i].index(' ')
            mmap[i] = mmap[i][:idx] + mmap[k] + (l2-l)*[' ']
            mmap[k] = l*[' ']
             
            break
    for i in tr:
        emptys.remove(i)
l = []
for i in mmap:
    l += mmap[i]

p2 = 0
for i,v in enumerate(l):
    if v != ' ':
        p2 += i*v
print(p2)