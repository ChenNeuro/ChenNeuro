class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, target_sum):
    if root is None:
        return False

    if root.left is None and root.right is None:  # The current node is a leaf node
        return root.val == target_sum

    left_exists = has_path_sum(root.left, target_sum - root.val)
    right_exists = has_path_sum(root.right, target_sum - root.val)

    return left_exists or right_exists


# Parse the input string and build a binary tree
def parse_tree(s):
    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit() or s[i] == '-':
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                j += 1
            num = int(s[i:j])
            node = TreeNode(num)
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
            i = j
        elif s[i] == '[':
            i += 1
        elif s[i] == ']' and s[i - 1] != '[' and len(stack) > 1:
            stack.pop()
            i += 1
        else:
            i += 1

    return stack[0] if len(stack) > 0 else None


while True:
    try:
        s = input()
    except:
        break

    s = s.split()
    target_sum = int(s[0])
    tree = ("").join(s[1:])
    tree = tree.replace('(', ',[').replace(')', ']')
    while True:
        try:
            tree = eval(tree[1:])
            break
        except SyntaxError:
            s = input().split()
            s = ("").join(s)
            s = s.replace('(', ',[').replace(')', ']')
            tree += s

    tree = str(tree)
    tree = tree.replace(',[', '[')
    if tree == '[]':
        print("no")
        continue

    root = parse_tree(tree)

    if has_path_sum(root, target_sum):
        print("yes")
    else:
        print("no")