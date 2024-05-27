def is_valid_pop_sequence(origin, output):
    if len(origin) != len(output):
        return False

    stack = []
    bank = list(origin)

    for char in output:
        while (not stack or stack[-1] != char) and bank:
            stack.append(bank.pop(0))

        if not stack or stack[-1] != char:
            return False

        stack.pop()

    return True


pushed = input()
while True:
    try:
        popped = input()
        if is_valid_pop_sequence(pushed, popped):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
