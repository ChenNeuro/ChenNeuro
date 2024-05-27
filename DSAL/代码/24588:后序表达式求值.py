def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token in "+-*/":
            right_operand = stack.pop()
            left_operand = stack.pop()
            if token == "+":
                stack.append(left_operand + right_operand)
            elif token == "-":
                stack.append(left_operand - right_operand)
            elif token == "*":
                stack.append(left_operand * right_operand)
            elif token == "/":
                stack.append(left_operand / right_operand)
        else:
            stack.append(float(token))
    return stack[0]


for i in range(int(input())):
    expression = input()
    # print(string)
    print("%.2f" % evaluate_postfix(expression))
