data = [[j for j in i] for i in open('4').read().strip().split('\n')]

p1 = 0
for line in data:
    for idx in range(len(line)):
        if idx+3<=len(data[0]):
            if line[idx:idx+4] == ['X', 'M', 'A', 'S'] or line[idx:idx+4] == ['S','A','M','X']:
                p1 += 1

for r in range(len(data)-3):
    for c in range(len(data[r])-3):
        if data[r][c]+data[r+1][c+1]+data[r+2][c+2]+data[r+3][c+3] == 'XMAS':
            p1 += 1
        if data[r][c]+data[r+1][c+1]+data[r+2][c+2]+data[r+3][c+3] == 'SAMX':
            p1 += 1

for r in range(len(data)-3):
    for c in range(len(data[r])-3):
        if data[r][c+3]+data[r+1][c+2]+data[r+2][c+1]+data[r+3][c+0] == 'XMAS':
            p1 += 1
        if data[r][c+3]+data[r+1][c+2]+data[r+2][c+1]+data[r+3][c+0] == 'SAMX':
            p1 += 1

data = list(map(list, zip(*data)))
for line in data:
    for idx in range(len(line)):
        if line[idx:idx+4] == ['X', 'M', 'A', 'S'] or line[idx:idx+4] == ['S','A','M','X']:
            p1 += 1

print(p1)
p2 = 0
for r in range(len(data)-2):
    for c in range(len(data[0])-2):
        lb,rb,ro,lo,m = data[r][c],data[r][c+2],data[r+2][c+2],data[r+2][c],data[r+1][c+1]
        if m == 'A':
            if ((lb,rb) == ('M','M') and (ro,lo) == ('S','S')) or ((lb,rb) == ('S','S') and (ro,lo) == ('M','M')):
                p2 += 1
            if (lb,lo)== ('M','M') and (rb,ro) == ('S','S') or (lb,lo) == ('S','S') and (rb,ro) == ('M','M'):
                p2 += 1
print(p2) 