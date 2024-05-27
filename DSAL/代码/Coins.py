# 23n2300010763，数院胡睿诚
'''
多重背包问题 (二进制优化)
多重背包问题通常可转化成01背包问题求解。但若将每种物品的数量拆分成多个1的话，时间复杂度会很高，
从而导致TLE。所以，需要利用二进制优化思想。即:一个正整数n，可以被分解成1,2,4,...,2^(k-1),
n-2^k+1的形式。其中，k是满足n-2^k+1>0的最大整数。
例如，假设给定价值为2，数量为10的物品，依据二进制优化思想可将10分解为1+2+4+3，则原来价值为2,
数量为10的物品可等效转化为价值分别为1*2，2*2，4*2，3*2，即价值分别为2，4，8，6，数量均为1的物品。

'''
import math


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ls = list(map(int, input().split()))
    w = (1 << (m + 1)) - 1                  #e.g., m=10, w=2047
    result = 1
    for i in range(n):
        number = ls[i+n] + 1                # e.g., number = 11
        limit = int(math.log(number, 2))    # limit = 3
        rest = number - (1 << limit)        # rest = 3
        for j in range(limit):
            result = (result | (result << (ls[i] * (1 << j)))) & w
        if rest > 0:
            result = (result | (result << (ls[i] * rest))) & w
    #print(sum_2(result) - 1)
    print(bin(result).count('1') - 1)