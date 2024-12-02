data = open('1').read().strip().split('\n')

l1 = []
l2 = []
for line in data:
    a,b = line.split('   ')
    l1.append(int(a))
    l2.append(int(b))

r2=r1=0
for a,b in zip(sorted(l1),sorted(l2)):
    c=l2.count(a)
    r1+= abs(a-b)
    r2+= a*c

print(r1)
print(r2)  