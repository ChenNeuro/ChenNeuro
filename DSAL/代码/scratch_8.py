"""
s = input()
s_l = len(s)
min_result = s_l + 1
table = [[-1]*102 for j in range(102)]


def ccount(sl,length):
    if table[sl][length] != -1:
        return table[sl][length]
    if length <= 1:
        return 0
    elif length == 2:
        if s[sl] == s[sl + 1]:
            return 0
        else:
            return 1
    else:
        if s[sl] == s[length+sl-1]:
            return ccount(sl+1, length - 2)
        min_result = length + 1
        tmp_result = min(ccount(sl, length - 1) + 1, ccount(sl+1, length - 1) + 1, ccount(sl+1, length - 2) + 1)
        if tmp_result < min_result:
            min_result = tmp_result
        table[sl][length] = min_result
        return min_result

print(ccount(0,s_l))
"""

"""
raw = input()
ans = 0
for a in range(0,len(raw)-3):
    a_raw = int(raw[0:a + 1])
    print(a_raw)
    if len(str(a_raw)) != a + 1:
        continue
    for b in range(a+1,len(raw)-2):
        b_raw = int(raw[a + 1:b + 1])
        print(b_raw)
        if len(str(b_raw)) != b - a:
            continue
        for c in range(b+1,len(raw)-1):
            c_raw = int(raw[b+1:c+1])
            print(c_raw)
            d_raw = int(raw[c+1:])
            print(d_raw)
            if len(str(c_raw)) != c-b and len(str(d_raw)) != len(raw) - c - 1:
                continue
            if a_raw <= 500 and b_raw <= 500 and c_raw <= 500 and d_raw <= 500:
                ans += 1
print(ans)
"""

"""
X= input()
Y = input()
a = len(X)
b = len(Y)
dp = [[0 for j in range(b+1)] for i in range(a+1)]
for i in range(1, a+1):  # 1-a的自然数列表
    for j in range(1, b+1):
        if X[i-1] == Y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1  # 这是递进程序
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 这是回溯程序
print(dp[a][b])
"""

"""
from collections import defaultdict


for _ in range(int(input())):
    dic = defaultdict(int)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(len(A)//2 - 1):
        dic[A[i*2 + 1]] += A[i*2]
    for j in range(len(B)//2 - 1):
        dic[B[j*2 + 1]] += B[j*2]
    ans = []
    for i in dic.items():
        if i[1] == 0:
            continue
        ans.append([i[1], i[0]])
    ans.sort(key=lambda x:(x[1]), reverse=True)
    print(" ".join(f"[ {i[0]} {i[1]} ]" for i in ans))
"""


def fun(m,n):
    # print(m,n)
    if m == 1 or n == 1 or m == 0:
        return 1
    if n > m:
        return fun(m,m)
    if n <= m:
        return fun(m-n,n) + fun(m,n-1)


m,n = map(int,input().split())
print(fun(m,n))
