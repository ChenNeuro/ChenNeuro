class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_node(nodes, parent, child):
    if parent not in nodes:
        nodes[parent] = Node(parent)
    if child not in nodes:
        nodes[child] = Node(child)
    nodes[parent].children.append(nodes[child])

def traverse(node):
    values = [node.value] + [child.value for child in node.children]
    values.sort()
    for value in values:
        if value == node.value:
            print(value)
        else:
            traverse(nodes[value])

# Parse the input
n = int(input())
nodes = {}
root = None
leaves = set()
for _ in range(n):
    line = list(map(int, input().split()))
    leaves |= set(line[1:])
    parent = line[0]
    if root is None:
        root = parent
    for child in line[1:]:
        add_node(nodes, parent, child)

for i in nodes.values():
    if i.value not in leaves:
        root = i.value
        break

# Traverse the tree
traverse(nodes[root])
# Path: 27928:遍历树.py