# Cheat Shit

```python
import statistics

```

1.  当然！Python 中的 **`statistics`** 模块提供了计算数值数据的数学统计函数。让我们来探讨一些关键的函数：
    1.  **`mean()`**：计算数据集的算术平均值（平均值）。
    2.  **`median()`**：查找数据集的中位数（中间值）。
    3.  **`mode()`**：确定离散或名义数据的单一众数（最常见的值）。
    4.  **`stdev()`**：计算数据的样本标准差。
    5.  **`variance()`**：计算数据的样本方差。

## String Opt

### 推荐模版：24591:中序表达式转后序表达式

```python
def infix_to_postfix(expression):
    stack = []
    postfix = []
    number = ""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    for char in expression:
        if char.isnumeric() or char == ".":
            number += char
        else:
            if number:
                num = float(number)
                postfix.append(int(num) if num.is_integer() else num)
                number = ""
            if char in "+-*/":
                while stack and stack[-1] in "+-*/" and precedence[stack[-1]] >= precedence[char]:
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
    if number:
        num = float(number)
        postfix.append(int(num) if num.is_integer() else num)

    while stack:
        postfix.append(stack.pop())

    return " ".join(str(x) for x in postfix)


n = int(input())
for _ in range(n):
    expression = input()
    print(infix_to_postfix(expression))
```

### 02694:波兰表达式

```python
num = -1


def step():
    global num
    num += 1
    if opt[num] == "+":
        return step() + step()
    elif opt[num] == "-":
        return step() - step()
    elif opt[num] == "*":
        return step() * step()
    elif opt[num] == "/":
        return step() / step()
    else:
        return float(opt[num])


opt = list(map(str,input().split()))
print("%.6f"%step())
```

### 十六进制

```python
def base_converter(dec_num, base):
    digits = "0123456789ABCDEF"
    
    rem_stack = [] # Stack()
    
    while dec_num > 0:
        rem = dec_num % base
        #rem_stack.push(rem)
        rem_stack.append(rem)
        dec_num = dec_num // base
        
    new_string = ""
    #while not rem_stack.is_empty():
    while rem_stack:
        new_string = new_string + digits[rem_stack.pop()]
        
    return new_string

print(base_converter(25, 2))
print(base_converter(2555, 16))

# 11001
# 9FB
```

## DFS

### 推荐模板：27310:积木

优美

```python
N = int(input())
block = [set(input()) for _ in range(4)]


def dfs(word):
    if len(word) == 0:
        return True
    for i in range(4):
        if not v[i]:
            if word[0] in block[i]:
                v[i] = True

                if dfs(word[1:]):
                    return True
                # 回溯
                v[i] = False

    return False


for i in range(N):
    s = input()
    n = len(s)
    v = [False] * 4
    if dfs(s):
        print("YES")
    else:
        print("NO")
```

## 栈

```python
def queen_stack(n):
    stack = []  # 用于保存状态的栈
    solutions = [] # 存储所有解决方案的列表

    stack.append((0, []))  # 初始状态为第一行，所有列都未放置皇后,栈中的元素是 (row, queens) 的元组

    while stack:
        row, cols = stack.pop() # 从栈中取出当前处理的行数和已放置的皇后位置
        if row == n:    # 找到一个合法解决方案
            solutions.append(cols)
        else:
            for col in range(n):
                if is_valid(row, col, cols): # 检查当前位置是否合法
                    stack.append((row + 1, cols + [col]))

    return solutions

def is_valid(row, col, queens):
    for r in range(row):
        if queens[r] == col or abs(row - r) == abs(col - queens[r]):
            return False
    return True


# 获取第 b 个皇后串
def get_queen_string(b):
    solutions = queen_stack(8)
    if b > len(solutions):
        return None
    b = len(solutions) + 1 - b

    queen_string = ''.join(str(col + 1) for col in solutions[b - 1])
    return queen_string

test_cases = int(input())  # 输入的测试数据组数
for _ in range(test_cases):
    b = int(input())  # 输入的 b 值
    queen_string = get_queen_string(b)
    print(queen_string)
```

