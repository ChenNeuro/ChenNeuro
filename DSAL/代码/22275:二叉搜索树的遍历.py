class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)
    elif value > root.val:
        root.right = insert(root.right, value)  #
    else:
        root.left = insert(root.left, value)
    return root


def postOrder(root):
    if root is None:
        return []
    return postOrder(root.left) + postOrder(root.right) + [root.val]


def levelOrder(root):
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return result


# N = int(input())
arr = list(map(int, input().split()))
vaild = set()
root = None
for value in arr:
    if value in vaild:
        continue
    vaild.add(value)
    root = insert(root, value)
print(*levelOrder(root))