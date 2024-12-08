from itertools import combinations
data = open('8').read().split('\n')

antennas = {}
antinodes = {}

for r,line in enumerate(data):
    for c,val in enumerate(line):
        if val != '.' and val in antennas:
            antennas[val].append((r,c))
        elif val != '.' and val not in antennas:
            antennas[val] = [(r,c)]

all_antinodes = []
for antenna in antennas:
    ants = antennas[antenna]
    anti = []
    for l,r in combinations(ants,2):
        r1,c1 = l
        r2,c2 = r
        dr = r1-r2
        dc = c1-c2
        a1 = (r1+dr,c1+dc)
        a2 = (r2-dr,c2-dc)
        if 0 <= a1[0] < len(data) and 0 <= a1[1] < len(data[0]):
            anti.append(a1)
        if 0 <= a2[0] < len(data) and 0 <= a2[1] < len(data[0]):
            anti.append(a2)
    if antenna in antinodes:
        antinodes[antenna] += anti
    else:
        antinodes[antenna] = anti
    all_antinodes += anti

print(len(set(all_antinodes)))

#part 2
all_antinodes = []
for antenna in antennas:
    ants = antennas[antenna]
    anti = []
    for l,r in combinations(ants,2):
        r1,c1 = l
        r2,c2 = r
        dr = r1-r2
        dc = c1-c2
        anti.append(l)
        a,b = r1-dr,c1-dc
        while 0 <= a < len(data) and 0 <= b < len(data[0]):
            anti.append((a,b))
            a -= dr;b-=dc
        a,b = r1+dr,c1+dc
        while 0 <= a < len(data) and 0 <= b < len(data[0]):
            anti.append((a,b))
            a += dr;b+=dc
    if antenna in antinodes:
        antinodes[antenna] += anti
    else:
        antinodes[antenna] = anti
    all_antinodes += anti

print(len(set(all_antinodes)))