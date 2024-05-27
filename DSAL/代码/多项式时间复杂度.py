string = list(map(str,input().split('+')))
top = 0
for i in string:
    if i[0] == '0':
        continue
    if i[0] == 'n':
        i = "1" + i
    tmp = list(map(int,i.split('n^')))
    top = max(top,int(tmp[-1]))
print(f'n^{top}')