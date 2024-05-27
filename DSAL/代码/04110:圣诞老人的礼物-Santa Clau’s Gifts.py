n, w = map(int, input().split())
candy = []
for i in range(n):
    cv, cw = map(int, input().split())
    candy.append((cv/cw, cw, cv))
candy.sort(reverse=True)
ans = 0

for i in candy:
    if i[1] > w:
        ans += w*i[0]
        print('%.1f' % ans)
        exit()
    else:
        ans += i[2]
        w -= i[1]
print('%.1f' % ans)