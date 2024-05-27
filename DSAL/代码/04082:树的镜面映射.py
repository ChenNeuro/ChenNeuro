from collections import deque


class TreeNode:
    def __init__(self, x):
        self.x = x  # 节点值
        self.children = []  # 子节点


def create_node():  # 创建节点
    return TreeNode('')


def build_tree(tempList, index):  # 构建多叉树 index为当前节点在tempList中的索引
    node = create_node()  # 创建节点
    node.x = tempList[index][0]  # 节点值
    if tempList[index][1] == '0' and node.x != '$':  # 如果节点值不为'$'且有子节点
        index += 1
        child, index = build_tree(tempList, index)  # 递归构建子节点
        node.children.append(child)  # 添加子节点
        index += 1
        child, index = build_tree(tempList, index)  # 递归构建子节点
        node.children.append(child)  # 添加子节点
    return node, index  # 返回当前节点及下一个节点的索引


def print_tree(p):  # 宽度优先遍历并打印镜像映射序列
    Q = deque()  # 队列Q
    s = deque()  # 栈s

    # 遍历右子节点并将非虚节点加入栈s
    while p is not None:
        if p.x != '$':
            s.append(p)
        p = p.children[1] if len(p.children) > 1 else None  # 右子节点

    # 将栈s中的节点逆序放入队列Q
    while s:
        Q.append(s.pop())

    # 宽度优先遍历队列Q并打印节点值
    while Q:
        p = Q.popleft()
        print(p.x, end=' ')

        # 如果节点有左子节点，将左子节点及其右子节点加入栈s
        if p.children:
            p = p.children[0]
            while p is not None:
                if p.x != '$':
                    s.append(p)
                p = p.children[1] if len(p.children) > 1 else None

            # 将栈s中的节点逆序放入队列Q
            while s:
                Q.append(s.pop())

# 读取输入
n = int(input())
tempList = input().split(' ')

# 构建多叉树
root, _ = build_tree(tempList, 0)

# 执行宽度优先遍历并打印镜像映射序列
print_tree(root)