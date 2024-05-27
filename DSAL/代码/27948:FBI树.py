class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_tree(s):
    if len(s) == 1:
        return TreeNode(s)
    top = TreeNode(s)
    top.left = build_tree(s[:len(s)//2])
    top.right = build_tree(s[len(s)//2:])
    return top


def postorder_traversal(root):
    if root is None:
        return ''
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    if set(root.val) == {'0'}:
        value = 'B'
    elif set(root.val) == {'1'}:
        value = 'I'
    else:
        value = 'F'
    return left + right + value


N = int(input())
print(postorder_traversal(build_tree(input())))