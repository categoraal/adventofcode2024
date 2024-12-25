data = open('25').read().strip().split('\n\n')
print(data)

keys = set()
locks = set()
for i in data:
    i = tuple(i.split('\n'))
    # print(i)
    # print(set(i[0]))
    # print(set(i[-1]))
    if set(i[0]) == {'#'} and set(i[-1]) == {'.'}:
        locks.add(i)
    if set(i[0]) == {'.'} and set(i[-1]) == {'#'}:
        keys.add(i)

# print(keys,locks)
print(len(keys))
print(len(locks))
hkeys = set()
hlocks = set()

for key in keys:
    l = []
    for c in range(5):
        r = 0
        while key[r][c] == '.':
            r += 1
        l.append(r-1)
    hkeys.add(tuple(l))

for lock in locks:
    l = []
    for c in range(5):
        r = 0
        while lock[r][c] == '#':
            r += 1
        l.append(r-1)
    hlocks.add(tuple(l))
print(len(hkeys))
print(len(hlocks))
p1 = 0
for lock in hlocks:
    for key in hkeys:
        # print(key,lock)
        s = 1
        for k,l in zip(key,lock):
            if k < l:s=0
        # break
        p1 += s
print(p1)
# print(hkeys)