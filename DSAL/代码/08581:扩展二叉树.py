class TreeNode:
    def __init__(self, x):
        self.v = x
        self.l = None
        self.r = None


index = 0


def tree_build(pre_order):
    global index
    if index >= len(pre_order) or pre_order[index] == ".":
        index += 1
        return None

    root = TreeNode(pre_order[index])
    index += 1
    root.l = tree_build(pre_order)
    root.r = tree_build(pre_order)
    return root


def midOrder(root):
    if root is None:
        return ''
    return midOrder(root.l) + root.v + midOrder(root.r)


def postOrder(root):
    if root is None:
        return ''
    return postOrder(root.l) + postOrder(root.r) + root.v


tree = input()
root = tree_build(tree)
print(midOrder(root))
print(postOrder(root))
