from collections import defaultdict
data = open('11').read()

data = [int(i) for i in data.split()]
counter = {}
for i,v in enumerate(data):
    counter[v] = 1


def blink2(x):
    res = defaultdict(int) 
    for i in x:
        cnt = x[i]
        if i == 0:
            res[1] += cnt
        elif len(str(i))%2 == 0:
            ln = len(str(i))//2
            l = int(str(i)[:ln])
            r = int(str(i)[ln:])
            res[l] += cnt
            res[r] += cnt
        else:
            res[i*2024] += cnt
    return res   
        
for i in range(75):
    counter = blink2(counter)
    if i in [24,74]:
        print(sum([counter[i] for i in counter]))