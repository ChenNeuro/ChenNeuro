class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def build(post, mid):
    if not post:
        return None
    root = TreeNode(post[-1])
    k = mid.index(post[-1])
    root.left = build(post[0:k], mid[:k])
    root.right = build(post[k:-1], mid[k+1:])
    return root

'''
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
    return ''.join(result)
'''


def preOrder(root):
    output = []
    if root:
        output.append(root.val)
        output.extend(preOrder(root.left))
        output.extend(preOrder(root.right))
    return output



mid = input()
post = input()
root = build(post, mid)
print(''.join(preOrder(root)))


# 2024.03.15 有点难度，需要多练习
