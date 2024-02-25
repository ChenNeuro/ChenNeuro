# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by ==陈奕好 工学院==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Sonoma 14.3.1 (c)

Python编程环境：PyCharm 2023.3.1 (Professional Edition)



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/practice/27653/



思路：类，真好用！



##### 代码

```python
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction(object):
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,other):
        newnum = self.num*other.den + other.num*self.den
        newden = self.den*other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

a,b,c,d = map(int,input().split())
f1 = Fraction(a,b)
f2 = Fraction(c,d)
f3=f1+f2
print(f3)
```



代码运行截图 ==（至少包含有"Accepted"）==

![Screenshot 2024-02-25 at 23.05.29](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-02-25 at 23.05.29.png)



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路： 重写了一遍，漏了一个退出条件。



##### 代码

```python
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
```



代码运行截图 ==（至少包含有"Accepted"）==

![Screenshot 2024-02-25 at 23.07.08](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-02-25 at 23.07.08.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：重写了一遍，还是有点细节第一遍没处理好。



##### 代码

```python
nCases = int(input())
for i in range(nCases):
    n, m, b = map(int, input().split())
    skills = []
    for j in range(n):
        ti, xi = map(int, input().split())
        skills.append((ti, xi))
    skills.sort(key=lambda x: (-x[0], x[1]))
    time = 1
    tm = m
    while skills and b > 0:
        ti, xi = skills.pop()
        if ti == time and tm > 0:
            b -= xi
            tm -= 1
        if ti > time:
            time = ti
            tm = m
            skills.append((ti, xi))
        if b <= 0:
            print(time)
            break
    if b > 0:
        print('alive')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-02-25 at 23.08.02](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-02-25 at 23.08.02.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：重写了一遍，没有MLE、TLE。



##### 代码

```python
import math
n = int(1e6)
ans = [False]*(n+1)
ans[1] = True
ans_list = set()
for i in range(2,int(math.sqrt(n+1)+1)):
    if not ans[i]:
        for j in range(i**2,n+1,i):
            ans[j]= True
for i in range(2,n+1):
    if not ans[i]:
        ans_list.add(i)

n = int(input())
nlist = list(map(int,input().split()))
for i in nlist:
    if math.pow(i,0.5) == int(math.pow(i,0.5)) and int(math.pow(i,0.5)) in ans_list:
        print("YES")
    else:
        print("NO")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-02-25 at 23.08.50](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-02-25 at 23.08.50.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：重写了一遍，发现子序列只能从两边删除。



##### 代码

```python
ans=[]
N=int(input())
for i in range(N):
    n,x=map(int,input().split())
    num=list(map(int,input().split()))
    if sum(num)%x != 0:
        ans.append(len(num))
    else:
        p, q = 0, 0
        num1 = num[::-1]
        for i in range(n):
            if num[i] % x != 0:
                p = i + 1
                break
        for i in range(n):
            if num1[i] % x != 0:
                q = i + 1
                break
        if p == 0 and q == 0:
            answer = -1
        else:
            answer = n - min(p,q)
        ans.append(answer)
for i in ans:
    print(i)


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-02-25 at 23.09.58](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-02-25 at 23.09.58.png)



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：没超时，集合赛高！



##### 代码

```python
n = int(1e4)
prime = [False]*(n+1)
prime[0] = False
prime[1] = True
ans_list = set()
for i in range(2,n+1):
    if not prime[i]:
        for j in range(i*i,n+1,i):
            prime[j] = True
for i in range(2,n+1):
    if not prime[i]:
        ans_list.add(i*i)
#print(ans_list)
m, n = map(int, input().split())
for i in range(m):
    temp = 0
    score = list(map(int, input().split()))
    for j in score:
        if j in ans_list:
            temp += j
    if temp == 0:
        print(0)
    else:
        print("%.2f" % (temp/len(score)))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-02-25 at 23.10.21](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-02-25 at 23.10.21.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

笑了，git在试图清空缓冲区的时候，直接pull了。重写了一遍，T1很重要！



