import math
string = input()
m = math.floor(math.log(len(string),2))
#print(m)
lst = []
ans = ""
for i in range(m+1):
    lst.append(string[2**i-1])
while len(lst) >= 2:
    ans += lst.pop(0)
    ans += lst.pop()
if lst:
    ans += lst[0]
print(ans)