from itertools import pairwise
wires,ins= open('24fixed').read().strip().split('\n\n')
wires = wires.split('\n')
ins = ins.split('\n')

gates = set()
values = {}
for i in wires:
    w,v = i.split()
    values[w[:-1]] = int(v)

logic = {}
resgates=[]
for i in ins:
    l,port,r,_,out = i.split()
    logic[out] = (l,r,port)   
    gates.add(l)
    gates.add(r)
    gates.add(out)
    if out.startswith('z'):
        resgates.append(out)

def solve(i):
    l,r,op = logic[i]
    if l in values: lv = values[l]
    else: lv = solve(l)
    if r in values: rv = values[r]
    else: rv = solve(r)

    if op == 'AND': 
        values[i] = lv & rv
        return values[i] 
    if op == 'XOR':
        values[i] = lv ^ rv
        return values[i] 
    if op == 'OR':
        values[i] = lv | rv
        return values[i]

# for i in range(46):
#     x = 'x'+str(i).zfill(2)
#     y = 'y'+str(i).zfill(2)
#     values[x] = 1
#     values[y] = 0

p1 = ''
for i in sorted(resgates,reverse=True):
    r = str(solve(i))
    p1 += r

# print(p1)
print(int(p1,2))

def connectedwires(i):
    l,r,op = logic[i]
    res = [l,r]
    if l in logic: res += connectedwires(l)
    if r in logic: res += connectedwires(r) 
    return res

# cnt = 0
# connected = {}
# l = []
# for idx,i in enumerate(sorted(resgates)):
#     if values[i] == 0:
#         cnt += 1

#     connected[i] = sorted(set(connectedwires(i)))
#     l.append(len(connected[i]))
    
# print(len(logic))


# for i,j in pairwise(sorted(resgates)):
#     print(j,set(connected[j])-set(connected[i]))
# print('t')

#gdd/z05/cwt/z09/jmv/css/pqt/z37

#part 2 mostly manual work
print(','.join(sorted(['gdd','z05','cwt','z09','jmv','css','pqt','z37'])))
