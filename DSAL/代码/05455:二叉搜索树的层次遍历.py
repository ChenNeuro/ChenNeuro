class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value < value:
            root.right = insert(root.right, value)
        elif root.value > value:
            root.left = insert(root.left, value)
    return root


def levelOrder(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(str(node.value))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ' '.join(result)


data = list(map(int, input().split()))
root = None
for value in data:
    root = insert(root, value)

# print(root.value)
print(levelOrder(root))

"""
def printTree(root, indent=""):
    if root is not None:
        printTree(root.right, indent + "   ")
        print(indent + str(root.value))
        printTree(root.left, indent + "   ")


# 在你的代码的最后，调用这个函数来打印树的结构：
printTree(root)
"""

