class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


def Tree_build(s):
    node = None
    stack = []  # for root
    for i in s:
        if i.isalpha():
            node = TreeNode(i)
            if stack:
                stack[-1].children.append(node)
        elif i == "(":
            stack.append(node)
            node = None
        elif i == ")":
            node = stack.pop()
        else:
            continue
    return node


def preorder(root):
    output = [root.val]
    for i in root.children:
        output.extend(preorder(i))
    return "".join(output)


def postorder(root):
    output = []
    for i in root.children:
        output.extend(postorder(i))
    output.append(root.val)
    return "".join(output)


s = input()
root = Tree_build(s)
print(preorder(root))
print(postorder(root))
