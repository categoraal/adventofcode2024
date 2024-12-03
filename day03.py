data = open('3').read().strip()

res= []
for i in range(len(data)):
    string = data
    if string[i:].startswith('mul('):
        f1 = True;f2 = True;f3 = False
        i += 4
        c1,c2 = '',''
        while f1: 
            if string[i].isnumeric() and f2:
                c1 += string[i]
            elif string[i] == ',' and f2:
                f3 = True
                f2 = False
            elif string[i].isnumeric() and f3:
                c2 += string[i]   
            elif string[i] == ')' and f3:
                res.append(int(c1)*int(c2))
                f1=f2=f3=False
            else:
                break
            i += 1
print(sum(res))

res = []
enable = True
dd = data.split('do()')
for k in dd:
    k = k.split("don't()")
    for i in range(len(k[0])):
        string = k[0]
        if string[i:].startswith('mul(') and enable:
            f1 = True;f2 = True;f3 = False
            i += 4
            c1,c2 = '',''
            while f1: 
                if string[i].isnumeric() and f2:
                    c1 += string[i]
                elif string[i] == ',' and f2:
                    f3 = True
                    f2 = False
                elif string[i].isnumeric() and f3:
                    c2 += string[i]   
                elif string[i] == ')' and f3:
                    res.append(int(c1)*int(c2))
                    f1=f2=f3=False
                else:
                    break
                i += 1

print(sum(res))