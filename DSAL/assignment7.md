# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

2024 spring, Complied by ==陈奕好 工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Sonoma 14.4 (23E214)

Python编程环境：PyCharm 2023.3.1 (Professional Edition)



## 1. 题目

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：简单题



代码

```python
arr = list(map(str,input().split()))
print(*arr[::-1])

```



代码运行截图 ==（至少包含有"Accepted"）==

![Screenshot 2024-04-03 at 23.45.33](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-04-03 at 23.45.33.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：滑动窗口



代码

```python
from collections import deque
M, N = map(int, input().split())
arr = list(map(int, input().split()))
window = deque()
ans = 0
for i in arr:
    if i in window:
        continue
    else:
        ans += 1
        if len(window) == M:
            window.popleft()
        window.append(i)
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![Screenshot 2024-04-04 at 00.01.16](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-04-04 at 00.01.16.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：感觉很trick，这个代码需要微调



代码

```python
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n or arr[k-1] < arr[k]:
    print(arr[k-1])
else:
    print(-1)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-04-04 at 00.09.28](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-04-04 at 00.09.28.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：FBI！这道题我问了几乎所有的ai，但几乎都过不了，甚至是一个很小的、可查的bug。判断FBI的板块死活放不对位置。



代码

```python
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_tree(s):
    if len(s) == 1:
        return TreeNode(s)
    top = TreeNode(s)
    top.left = build_tree(s[:len(s)//2])
    top.right = build_tree(s[len(s)//2:])
    return top


def postorder_traversal(root):
    if root is None:
        return ''
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    if set(root.val) == {'0'}:
        value = 'B'
    elif set(root.val) == {'1'}:
        value = 'I'
    else:
        value = 'F'
    return left + right + value


N = int(input())
print(postorder_traversal(build_tree(input())))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-04-04 at 00.10.12](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-04-04 at 00.10.12.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：字典里套用deque()的想法第一次实现



代码

```python
from collections import deque

t = int(input())
teams = {i: deque(map(int, input().split())) for i in range(t)}
queue = deque()
group_queue = {i: deque() for i in range(t)}

while True:
    command = input().split()
    if command[0] == 'STOP':
        break
    elif command[0] == 'ENQUEUE':
        person = int(command[1])
        for i in range(t):
            if person in teams[i]:
                group_queue[i].append(person)
                if i not in queue:
                    queue.append(i)
                break
    elif command[0] == 'DEQUEUE':
        group = queue[0]
        print(group_queue[group].popleft())
        if not group_queue[group]:
            queue.popleft()


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-04-04 at 00.19.23](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-04-04 at 00.19.23.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：字典重要性史诗级增强！！！！！！！！！！！！！

在建树的时候将value与树建立关系



代码

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_node(nodes, parent, child):
    if parent not in nodes:
        nodes[parent] = Node(parent)
    if child not in nodes:
        nodes[child] = Node(child)
    nodes[parent].children.append(nodes[child])

def traverse(node):
    values = [node.value] + [child.value for child in node.children]
    values.sort()
    for value in values:
        if value == node.value:
            print(value)
        else:
            traverse(nodes[value])

# Parse the input
n = int(input())
nodes = {}
root = None
leaves = set()
for _ in range(n):
    line = list(map(int, input().split()))
    leaves |= set(line[1:])
    parent = line[0]
    if root is None:
        root = parent
    for child in line[1:]:
        add_node(nodes, parent, child)

for i in nodes.values():
    if i.value not in leaves:
        root = i.value
        break

# Traverse the tree
traverse(nodes[root])

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![Screenshot 2024-04-04 at 00.27.23](/Users/chenyihao/Library/Application Support/typora-user-images/Screenshot 2024-04-04 at 00.27.23.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

没时间当堂考，字典重要性突然增强，之前一直被value与树的联系犯难，现在出现了这个东西。


$$
list(dict[i])
$$

$$
dict[i] = list
$$

这是个可删除dict[i],方便对list进行管理，且 $dict[i]$ 也可以是动态的。

