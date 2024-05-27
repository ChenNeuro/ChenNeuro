"""
N, M = map(int, input().split())
dp = ([0] * (N+1))
dp[0] = 1
for i in range(1, N+1):
    if i < M:
        dp[i] = dp[i-1]*2
    elif i == M:
        dp[i] = dp[i-1]*2 - 1
    else:
        dp[i] = dp[i-1]*2 - dp[i - M - 1]
print(dp[N])
"""


"""
import math
ls = set()
for i in range(1,100):
    ls.add(i**2)
m = input()
l = list(map(int, input().split()))
for i in l:
    for j in ls:
        if (i - j) in ls:
            print(bin(i),oct(i),hex(i))
            break
"""


"""
ls = list(map(int, input().split()))
ls.sort()
l = len(ls)
q = set()
for i in range(0,l-2):
    if i>0 and ls[i] == ls[i-1]:
        continue
    d = {}
    for j in ls[i+1:]:
        if j not in d:
            d[-ls[i] - j] = 1
        else:
            q.add((ls[i], -ls[i]-j, j))
print(len(q))
"""


"""
L, N, M = map(int, input().split())
stone = [0]
for i in range(N):
    stone.append(int(input()))
stone.append(L)

def check(x):
    num, s = 0, 0
    for i in range(1,N+2):
        if stone[i] - s < x:
            num += 1
        else:
            s = stone[i]
    return [False, True][num > M]

lo = 0
hi = L + 1
ans = -1
while lo < hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid
    else:
        ans = mid
        lo = mid + 1

print(ans)
"""


"""
import math
n = int(2000)
ans = [False] * (n+1)
ans[1] =True
ans_list = []
for i in range(2,int(math.sqrt(n+1)+1)):
    if not ans[i]:
        for j in range(i*i, n+1, i):
            ans[j] = True
for i in range(2,n+1):
    if not ans[i]:
        ans_list.append(i)

res = []
x = int(input())
if x < 6 or x % 2 != 0:
    print('Error!')
else:
    for i in ans_list:
        if 2*i <= x and x-i in ans_list:
            res.append(f'{x}={i}+{x-i}')
    for i in res:
        print(i)
"""


"""
matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    maxium = max(matrix[i])
    for j in range(5):
        if maxium == matrix[i][j]:
            tag = True
            for k in range(5):
                if matrix[k][j] < maxium:
                    tag = False
            if tag:
                print(i+1,j+1,maxium)
                exit()
print("not found")
"""

"""
def sgn(x):
    if x < -1:
        return -1
    elif x > 1:
        return 1
    else:
        return 0


n = int(input())
l1 = list(map(int, input().split()))
l2 = [l1[i] - l1[i-1] for i in range(1, n)]
if n == 1:
    print(1)
    exit()
ans = 1
sign = 0
for i in range(n-1):
    if l2[i]*sign < 0 or (sign == 0 and l2[i] != 0):
        ans += 1
        sign = l2[i]
print(ans)
"""

"""
nCases = int(input())
for _ in range(nCases):
    n, m, b = map(int, input().split())
    t_x = []
    for i in range(n):
        ti_xi = list(map(int, input().split()))
        t_x.append(ti_xi)
    t_x.sort(key=lambda x:(x[0],-x[1]))
    turn = t_x[0][0]
    mt = m
    tag = False
    for i in range(n):
        if t_x[i][0] != turn:
            turn = t_x[i][0]
            mt = m
        if mt > 0:
            mt -= 1
            b -= t_x[i][1]
        if b <= 0:
            tag = True
            break
    if tag:
        print(turn)
    else:
        print("alive")
"""


"""
from collections import deque
while True:
    n ,m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    l = [i for i in range(1,n+1)]
    cnt = 1
    queue = deque(l)
    while len(queue) != 1:
        a = queue.popleft()
        if cnt == m:
            cnt = 1
            continue
        else:
            cnt += 1
            queue.append(a)
    print(queue[0])
"""


"""
n = int(input())
cmp = []
for i in range(n):
    cmp.append(list(map(int, input().split())))
cmp.sort(key=lambda x:(-x[1],x[0]))
ans1 = ans2 = 0
for i in range(n):
    ans1 += cmp[i][0]
    ans2 = max(ans2, ans1 + cmp[i][1])
print(ans2)
"""

"""
from math import ceil
n = int(input())
matrix = [0 for _ in range(n)]
for i in range(n):
    matrix[i] = [int(_) for _ in input().split()]
ans = [0] * ceil(n/2)
for i in range(n):
    for j in range(n):
        ans[min(i, j, n-1-i, n-1-j)] += matrix[i][j]  # 这和n皇后异曲同工
print(max(ans))
"""


"""
r=list(input())
n=len(r)
R=[0]*n
B=[0]*n
if r[0]=="R":R[0]=0;B[0]=1
else:R[0]=1;B[0]=0
for i in range(n-1):
    if r[i+1]=="R":
        R[i+1]=R[i]
        B[i+1]=min(R[i],B[i])+1
    else:
        R[i+1]=min(R[i],B[i])+1
        B[i+1]=B[i]
print(R[-1])
"""


"""
# 多重背包中的最优解问题
n, m = map(int,input().split())
price = list(map(int,input().split()))
nums = list(map(int, input().split()))
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(m):
#for i in range(6, -1, -1):
    cur_price = price[i]
    cur_num = nums[i]
    k = 1
    while cur_num > 0:  #二进制分组优化，时间缩短了将近两个数量级。
#相同物品避免重复工作，「二进制分组」提高效率。
        use_num = min(cur_num, k)
        cur_num -= use_num
        for j in range(n, cur_price * use_num - 1, -1):
            dp[j] = min(dp[j], dp[j - cur_price * use_num] + use_num)
        k *= 2
if dp[-1] == float('inf'):
    print('Fail')
else:
    print(dp[-1])  # dp中包含了所有可能
"""


"""
def check(num):
    if num % 19 == 0 or "19" in str(num):
        return True
    return False
for i in range(int(input())):
    if check(int(input())):
        print("Yes")
    else:
        print("No")
"""


"""
from collections import Counter
word = ""
for i in range(4):
    word += input()
word_count = Counter(word)
maxium = 0
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if word_count[i] > maxium:
        maxium = word_count[i]
l = [[" "]*(maxium+1) for _ in range(26)]

for i, pos in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    l[i][-1] = pos
for i, pos in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if pos in word_count:
        for j in range(2, 2+word_count[pos]):
            l[i][-j] = "*"

l_zip = list(zip(*l))
for i in range(len(l_zip)):
    print(" ".join(l_zip[i][j] for j in range(26)))
"""


"""
import re

word = input().lower()
article = input().lower()

a = re.findall(r'\b'+word+r'\b', article)
cnt = len(a)
if cnt == 0:
    print(-1)
else:
    aa  = re.search(r'\b'+word+r'\b', article)
    print(cnt, aa.start())
"""


"""
m,n=map(int,input().split())
heightMap = [list(map(int, input().split())) for _ in range(m)]



def trapRainWater():
    m, n = len(heightMap), len(heightMap[0])
    maxHeight = max(max(row) for row in heightMap)
    water = [[maxHeight for _ in range(n)] for _ in range(m)]
    dirs = [-1, 0, 1, 0, -1]

    qu = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                if water[i][j] > heightMap[i][j]:
                    water[i][j] = heightMap[i][j]
                    qu.append([i, j])

    while len(qu) > 0:
        [x, y] = qu.pop(0)
        for i in range(4):
            nx, ny = x + dirs[i], y + dirs[i + 1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if water[x][y] < water[nx][ny] and water[nx][ny] > heightMap[nx][ny]:
                water[nx][ny] = max(water[x][y], heightMap[nx][ny])
                qu.append([nx, ny])

    ans = 0
    for i in range(m):
        for j in range(n):
            ans = ans + water[i][j] - heightMap[i][j]
    return ans



print(trapRainWater())
"""


"""
n = int(input())
if n % 4 == 0:
    if n % 100 == 0 and n % 400 != 0:
        print("N")
        exit()
    if n % 3200 == 0:
        print("N")
        exit()
    print("Y")
else:
    print("N")
"""

# 按照整数划分来做
'''
递推式：
如果i为奇数：那么它一定可以由f[i-1]转移过来，是前面的那个数所有方案里都加了一个1

如果i为偶数：它可以看成是f[i-2]中的方案加了一个2，或者是f[i/2]的方案里乘了一个2；
所以应该是f[i-2]和f[i/2]的和

'''


"""
MOD = 10**9
N = int(input())
dp = [1] + [0]*N
for i in range(1, N+1):
    if i & 1:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-2] + dp[i//2]) % MOD #

print(dp[-1])
"""


n = int(input())
minium = 61
act = []
for i in range(n):
    x, y = map(int, input().split())
    minium = min(minium,x)
    act.append((x, y))
dp = [0]*61
if minium == 0:
    dp[0] = 1
for i in range(1,61):
    dp[i] = dp[i-1]
    for start,end in act:
        if end == i:
            dp[i] = max(dp[i],dp[start-1]+1)
            print(dp)
print(dp[-1])

