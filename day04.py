data = open('4').read().strip().split('\n')

p1 = 0
ds = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'X':
            for di,dj in ds:
                if 0<= i+3*di<len(data) and 0 <=j+3*dj<len(data[0]):
                    if data[i+di][j+dj]+data[i+2*di][j+2*dj]+data[i+3*di][j+3*dj] == 'MAS':
                        p1 += 1
print(p1)

p2 = 0
for r in range(len(data)-2):
    for c in range(len(data[0])-2):
        lb,rb,ro,lo,m = data[r][c],data[r][c+2],data[r+2][c+2],data[r+2][c],data[r+1][c+1]
        if m == 'A':
            if ''.join([lb,rb,ro,lo]) in ['MMSS','SMMS','SSMM','MSSM']:p2+=1
print(p2) 