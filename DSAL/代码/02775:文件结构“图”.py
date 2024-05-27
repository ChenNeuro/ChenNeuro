def print_dir(dir, indent):
    print('|     ' * indent + dir[0])
    for sub_dir in dir[1]:
        print_dir(sub_dir, indent + 1)
    for file in sorted(dir[2]):
        print('|     ' * indent + file)


def solve():
    stack = [['ROOT', [], []]]
    dataset = 1
    while True:
        line = input().strip()
        if line == "#":
            break
        elif line == '*':
            print('DATA SET {}:'.format(dataset))
            print_dir(stack[0], 0)
            print()
            stack = [['ROOT', [], []]]
            dataset += 1
        elif line[0] == 'd':
            stack.append([line, [], []])
        elif line[0] == 'f':
            stack[-1][2].append(line)
        elif line == ']':
            dir = stack.pop()
            stack[-1][1].append(dir)


solve()


