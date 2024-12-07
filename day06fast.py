import time
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
a = time.time()
data = open('6').read().split('\n')


from collections import defaultdict
kaart = {}
rows= defaultdict(list) 
cols = defaultdict(list)
blocks = []
for r,v in enumerate(data):
    for c,v2 in enumerate(v):
        kaart[(r,c)] = v2
        if v2 == '#':
            rows[r].append(c)
            cols[c].append(r)
            blocks.append((r,c))
        if v2 == '^':
            start = (r,c) 

for r in range(len(data)):
    rows[r] = [-2]+rows[r]+[len(data)+2]
for c in range(len(data[0])):
    cols[c] = [-2]+cols[c]+[len(data[0])+2]

dr,dc = -1,0
for _ in range(4):
    (dr,dc) = dc,-dr

def walk():
    r,c = start
    dr,dc= -1,0
    l = 0
    seen = set()

    while True:      
        if dr == -1:
            cs = cols[c]
            for i in cs[::-1]:
                if i < r:
                    l += (r-i-1)
                    for p in range(r,i,-1):
                        seen.add((p,c))
                    r,c = i+1,c
                    break
        elif dr == 1:
            cs = cols[c]
            for i in cs:
                if i > r:
                    l += (i+1-r)
                    for p in range(r,i):
                        seen.add((p,c))
                    r,c = i-1,c
                    break
        elif dc == -1:
            rs = rows[r]
            for i in rs[::-1]:
                if i < c:
                    l += (c-i-1)
                    for p in range(c,i,-1):
                        seen.add((r,p))
                    r,c = r,i+1
                    break
        elif dc == 1: 
            rs = rows[r]
            for i in rs:
                if i > c:
                    l += (i+1-c)
                    for p in range(c,i):
                        seen.add((r,p))
                    r,c = r,i-1
                    break 
        (dr,dc) = dc,-dr
        if r < 0 or r > len(data) or c < 0 or c > len(data):
            break
    return seen

# print(len(seen)-2)
# print(time.time()-a)

def walk2(p):
    r,c = start
    dr,dc= -1,0
    br,bc = p
    if p == start:
        return 0
    # rows[br].append(bc)
    # rows[br] = sorted(rows[br])
    # cols[bc].append(br)
    # cols[bc] = sorted(cols[bc])
    seen = set((r,c,dr,dc))
    while True:      
        if dr == -1:
            cs = cols[c]
            for i in cs[::-1]:
                if i < r:
                    if c == bc and i < br < r:
                        i = br
                    r,c = i+1,c
                    break
        elif dr == 1:
            cs = cols[c]
            for i in cs:
                if i > r:
                    if c == bc and i > br > r:
                        i = br
                    r,c = i-1,c
                    break
        elif dc == -1:
            rs = rows[r]
            for i in rs[::-1]:
                if i < c:
                    if r == br and i < bc < c:
                        i = bc
                    r,c = r,i+1
                    break
        elif dc == 1: 
            rs = rows[r]
            for i in rs:
                if i > c:
                    if r == br and i > bc > c:
                        i = bc
                    r,c = r,i-1
                    break 
        (dr,dc) = dc,-dr
        if (r,c,dr,dc) in seen:
            # rows[br].remove(bc)
            # cols[bc].remove(br)
            return 1
        seen.add((r,c,dr,dc))
        if r < 0 or r > len(data) or c < 0 or c > len(data):
            # rows[br].remove(bc)
            # cols[bc].remove(br)
            return 0
# if __name__ == '__main__':
#     with Pool(6) as p:
#         p2 = sum(p.map(walk2,seen))
#         print(p2-2)

# def main():
#     a = time.time()
#     seen = walk()
#     print(len(seen)-2)
#     print(time.time()-a)
#     b = time.time()
#     with ThreadPoolExecutor() as executor:
#         # Map each item in the list to f2 in parallel
#         p2 = sum(executor.map(walk2, seen))
#     print(time.time()-b)
    
    # print(p2)

def main():
    a = time.time()
    seen = walk()
    print(len(seen)-2)
    print(time.time()-a)
    b = time.time()
    with Pool(6) as p:
        p2 = sum(p.map(walk2,seen))
    print(p2-2)
    print(time.time()-b)
    

if __name__ == "__main__":
    main()

# a = time.time()
# seen = walk()
# print(len(seen)-2)
# print(time.time()-a)
# b = time.time()
# p2 = sum(map(walk2,seen))
# print(p2-2)
# print(time.time()-b)