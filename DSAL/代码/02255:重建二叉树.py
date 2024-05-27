class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def rebuild(pre, mid):
    if not pre:
        return None
    node = TreeNode(pre[0])
    k = mid.index(pre[0])
    node.left = rebuild(pre[1:k+1], mid[:k])
    node.right = rebuild(pre[k+1:], mid[k+1:])
    return node


def postOrder(root):
    if root is None:
        return []
    return postOrder(root.left) + postOrder(root.right) + [root.val]


while True:
    try:
        pre, mid = input().split()
        root = rebuild(pre, mid)
        print("".join(postOrder(root)))
    except EOFError:
        break
