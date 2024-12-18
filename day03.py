data = open('3').read().strip()

p1 = p2 = 0
enable = True
for i in range(len(data)):
    if data[i:].startswith("do()"):
        enable = True
    if data[i:].startswith("don't()"):
        enable = False
    if data[i:].startswith('mul('):
        f1 = f2=True;f3 = False
        i += 4
        c1=c2 = ''
        while f1: 
            if data[i].isnumeric() and f2:
                c1 += data[i]
            elif data[i] == ',' and f2:
                f3 = True
                f2 = False
            elif data[i].isnumeric() and f3:
                c2 += data[i]   
            elif data[i] == ')' and f3:
                p1 += int(c1)*int(c2)
                if enable:
                    p2 += int(c1)*int(c2)
                f1 = False
            else:
                break
            i += 1

print(p1)
print(p2)

import re
# x = re.findall(r'mul\(\d+,\d+\)',data)
print(sum([a*b for a,b in [[int(i) for i in re.findall(r'\d+',line)] for line in re.findall(r'mul\(\d+,\d+\)',open('3').read())]]))

print(sum((int(i or 0)*int(j or 0) for i,j in re.findall(r'(?s)(?:(?<=don\'t\(\)).*?(?=do\(\)|$))|(?:mul\((\d+),(\d+)\))',data))))