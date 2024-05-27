def infix_to_postfix(expression):
    stack = []  # operators and "("
    postfix = []  # ans
    number = ""
    precedence = {"!": 2, "|": 1, "&": 1}

    for char in expression:
        # if char.isnumeric() or char == ".":
        if char.isalpha():
            number += char
        else:
            if number:  # number is not empty
                postfix.append(number)
                number = ""  # reset number

            if char == "!":  # unary operator
                if stack and stack[-1] == "!":  # 减少了递归，每次都处理
                    stack.pop()
                    continue
            # 关于优先级， 1. 优先级高的先出栈 2. 优先级相同的，先入栈的先出栈
            if char in ["!", '|', '&']:
                while stack and stack[-1] in ['!', '|', '&'] and precedence[stack[-1]] >= precedence[char]:
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
    if number:
        postfix.append(number)

    while stack:
        postfix.append(stack.pop())

    return " ".join(str(x) for x in postfix)


def calculate_postfix(postfix_expression):
    stack = []
    for char in postfix_expression.split():
        if char == "V":
            stack.append(True)
        elif char == "F":
            stack.append(False)
        elif char == "!":
            operand = stack.pop()
            stack.append(not operand)
        elif char == "&":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 and operand2)
        elif char == "|":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 or operand2)
    return "V" if stack.pop() else "F"


while True:
    try:
        expression = input()
        postfix_expression = infix_to_postfix(expression)
        print(calculate_postfix(postfix_expression))
    except EOFError:
        break
