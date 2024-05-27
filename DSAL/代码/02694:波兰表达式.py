"""
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
"""


opt = list(map(str, input().split()))
stack = []
for i in range(len(opt)-1, -1, -1):
    if opt[i] == "+":
        stack.append(stack.pop() + stack.pop())
    elif opt[i] == "-":
        stack.append(stack.pop() - stack.pop())
    elif opt[i] == "*":
        stack.append(stack.pop() * stack.pop())
    elif opt[i] == "/":
        a, b = stack.pop(), stack.pop()
        stack.append(a/b)
    else:
        stack.append(float(opt[i]))
    print(stack)
print("%.6f" % stack[0])