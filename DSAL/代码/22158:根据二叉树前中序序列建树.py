class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def build(pre, mid):
    if not pre:
        return None
    root = TreeNode(pre[0])
    k = mid.index(pre[0])
    root.left = build(pre[1:k+1], mid[:k])
    root.right = build(pre[k+1:], mid[k+1:])
    return root


def postOrder(root):
    output = []
    if root.left:
        output.extend(postOrder(root.left))
    if root.right:
        output.extend(postOrder(root.right))
    output.append(root.val)
    return "".join(output)


while True:
    try:
        pre = input()
        mid = input()
        root = build(pre, mid)
        print(postOrder(root))

    except EOFError:
        break

# 2024.03.15 有点难度，需要多练习
