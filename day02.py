data = [line.split() for line in open('2').read().strip().split('\n')]

def isSave(x):
    x = [int(i) for i in x]
    cn = len(x)-1
    a = x[0]
    c = []
    for i in x[1:]:
        n = a-i
        c.append(n)
        a = i

    check = [1 for i in c if -3 <= i <= -1]
    if sum(check) == cn:
        return 1
    check = [1 for i in c if 1 <= i <= 3]
    if sum(check) == cn:
        return 1
    return 0 

unsave = []
cnt_save= 0
for line in data:
    n = isSave(line)
    cnt_save += n
    if n != 1:
        unsave.append(line)
         
print(cnt_save)

for line in unsave:
    c = False
    for i in range(len(line)):
        l = line[:i]+line[i+1:]
        if isSave(l): 
            c = True
    if c:
        cnt_save += 1
         
print(cnt_save)
        