from collections import defaultdict
N = int(input())
ans = defaultdict(int)
for _ in range(N):
    web, start, end = list(map(str, input().split()))
    hour1, min1, sec1 = list(map(int, start.split(":")))
    hour2, min2, sec2 = list(map(int, end.split(":")))
    time = (hour2 - hour1) * 3600 + (min2 - min1) * 60 + (sec2 - sec1)
    # print(time)
    ans[web] += time
# print(ans)
print(max(ans, key=ans.get))
# print(ans)
