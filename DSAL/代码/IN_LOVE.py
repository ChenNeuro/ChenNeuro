'''
The claim is that if the answer exists, we can take the segment with
the minimum right boundary and the maximum left boundary
(let's denote these boundaries as 𝑟 and 𝑙). Therefore, if 𝑟<𝑙
, it is obvious that this pair of segments is suitable for us.
Otherwise, all pairs of segments intersect because they have common
points in the range 𝑙…𝑟.

先写了个超时的算法，然后看tutorial及其他人引入dict, heap的代码。
按照区间右端点从小到大排序。从前往后依次枚举每个区间。
假设当前遍历到的区间为第i个区间 [li, ri]，如果有li > ed，
说明当前区间与前面没有交集。
'''

import sys
import heapq
from collections import defaultdict  # 这是一个特殊的dict，不存在的索引也不报错，而且可以返回一个初始值

input = sys.stdin.readline  # 提速-1

minH = []
maxH = []

ldict = defaultdict(int)  # 这里索引不存在时，返回的就是0，提速-2
rdict = defaultdict(int)  # 这里索引不存在时，返回的就是0，提速-3

n = int(input())

for _ in range(n):
    op, l, r = map(str, input().strip().split())
    l, r = int(l), int(r)
    if op == "+":
        ldict[l] += 1
        rdict[r] += 1
        heapq.heappush(maxH, -l)  # 提速-4
        heapq.heappush(minH, r)  # 维护maxH， minH，提速-5
    else:
        ldict[l] -= 1
        rdict[r] -= 1  # 维护maxH， minH

    '''
    使用 while 循环，将最大堆 maxH 和最小堆 minH 中出现次数为 0 的边界移除。
    # 由于每次比的是最大最小项，故需要判断的是第一个出现次数非0的最大最小项
    通过比较堆顶元素的出现次数，如果出现次数为 0，则通过 heappop 方法将其从堆中移除。
    '''
    while len(maxH) > 0 >= ldict[-maxH[0]]:  # 0是maxH（存的是负数）中最大一项
        heapq.heappop(maxH)
    while len(minH) > 0 >= rdict[minH[0]]:
        heapq.heappop(minH)

    '''
    判断堆 maxH 和 minH 是否非空，并且最小堆 minH 的堆顶元素是否小于
    最大堆 maxH 的堆顶元素的相反数。
    '''
    if len(maxH) > 0 and len(minH) > 0 and minH[0] < -maxH[0]:
        print("Yes")
    else:
        print("No")

# 左一定小于右，若有题中要求的结构，则有右小于左边，为什么不用最小的右边比较最大的左边呢？（反问）
# 同时要记得dict会减到0，及时删除0项
# 为什么不只保留最大值，最小值呢？因为如果被删除了就得找次小值，和次大值
# heap的好处，就是时刻维护一个最大值，但heap改变了索引，索引变得无序
# 但这里不需要考虑每组数据的位置，因为它删除的时候就告诉你位置，所以可以用字典来访问
