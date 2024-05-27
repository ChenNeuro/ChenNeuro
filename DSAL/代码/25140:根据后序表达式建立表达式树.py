class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ''.join(result[::-1])


def build(s):

    stack = []
    for i in s:
        if i.islower():
            node = TreeNode(i)
            stack.append(node)
        else:
            node = TreeNode(i)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[0]


for i in range(int(input())):
    s = input()
    root = build(s)
    ans = ""
    for _ in levelOrder(root):
        ans += ("".join(_))
    print(ans)