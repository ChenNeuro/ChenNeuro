class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1


def insert(root, value):
    if root is None:
        return TreeNode(value)
    elif value > root.val:
        root.right = insert(root.right, value)  #
    else:
        root.left = insert(root.left, value)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    # 如果节点失衡，那么有4种情况需要处理
    # Case 1 - 左左
    if balance > 1 and value < root.left.val:
        return right_rotate(root)

    # Case 2 - 右右
    if balance < -1 and value > root.right.val:
        return left_rotate(root)

    # Case 3 - 左右
    if balance > 1 and value > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case 4 - 右左
    if balance < -1 and value < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def get_height(root):
    if root is None:
        return 0
    else:
        return root.height


def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)


def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


def preOrder(root):
    if root is None:
        return []
    return [root.val] + preOrder(root.left) + preOrder(root.right)


N = int(input())
arr = list(map(int, input().split()))

root = None
for value in arr:
    root = insert(root, value)
# print(get_height(root))
print(*preOrder(root))
# print(*ans)
