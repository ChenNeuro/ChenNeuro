class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrder(root):
    if root is None or root.val == '*':
        return []
    return [root.val] + preOrder(root.left) + preOrder(root.right)

def postOrder(root):
    if root is None or root.val == '*':
        return []
    return postOrder(root.left) + postOrder(root.right) + [root.val]

def inOrder(root):
    if root is None or root.val == '*':
        return []
    return inOrder(root.left) + [root.val] + inOrder(root.right)


def createTree(lines):
    stack = []
    for line in lines:
        level = line.count("-")
        val = line[level]
        node = TreeNode(val)
        while len(stack) > level:
            stack.pop()
        if stack and stack[-1].left is None:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0]


n = int(input())
for _ in range(n):
    lines = []
    while True:
        line = input().strip()
        if line == '0':
            break
        lines.append(line)
    root = createTree(lines)
    print(''.join(preOrder(root)))
    print(''.join(postOrder(root)))
    print(''.join(inOrder(root)))
    print()