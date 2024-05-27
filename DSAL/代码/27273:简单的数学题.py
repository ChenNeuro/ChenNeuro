import math
t = int(input())
for i in range(t):
    n = int(input())
    ans = n*(n+1)//2
    # print(ans)
    for j in range(0,math.floor(math.log(n,2)) + 1):
        ans -= 2 * (2**j)
        # print(ans)
    print(ans)