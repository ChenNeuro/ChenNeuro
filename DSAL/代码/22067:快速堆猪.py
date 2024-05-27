"""
class pig_stack():
    def __init__(self):
        self.stack = []

    def push(self, new):
        self.stack.append(new)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def min(self):
        if len(self.stack):
            return min(self.stack)
        return False


stack1 = pig_stack()
while True:
    try:
        opt = list(map(str, input().split()))
        if opt[0] == 'push':
            stack1.push(int(opt[1]))
        elif opt[0] == 'pop':
            stack1.pop()
        elif opt[0] == 'min':
            if stack1.min():
                print(stack1.min())
    except EOFError:
        break
"""


"""
stack = []
minValue = []
while True:
    try:
        opt = list(map(str, input().split()))
        if opt[0] == 'push':
            x = int(opt[1])
            if minValue:
                if minValue[-1] >= x:
                    minValue.append(x)
            else:
                minValue.append(x)
            stack.append(x)
        elif opt[0] == 'pop':
            if stack:
                if stack[-1] == minValue[-1]:
                    minValue.pop()
                stack.pop()
        elif opt[0] == 'min':
            if stack:
                print(minValue[-1])
    except EOFError:
        break
"""


stack = []
m_list = []
while True:
    try:
        opt = input().split()
        if opt[0] == "pop":
           if stack:
                out_ = stack.pop()
                if m_list[-1] == out_:
                    m_list.pop()
                # print(out)

        elif opt[0] == "min":
            if stack:
                print(m_list[-1])

        else:
            in_ = int(opt[1])
            stack.append(in_)
            if m_list:
                if in_ <= m_list[-1]:
                    m_list.append(in_)
            else:
                m_list.append(in_)

    except EOFError:
        break
