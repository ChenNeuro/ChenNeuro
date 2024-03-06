# Cheat Shit

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