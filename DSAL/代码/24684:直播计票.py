from collections import Counter
string = map(int,input().split())
counter = Counter(string)
maxium = max(counter.values())
ans = []

for i in list(counter.items()):
    if i[1] == maxium:
        ans.append(i[0])
ans.sort()
print(*ans)
