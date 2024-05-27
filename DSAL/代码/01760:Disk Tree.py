def insert(node, path):
    for dir in path:
        if dir not in node:
            node[dir] = {}
        node = node[dir]

def print_tree(node, indent=0):
    for dir in sorted(node):
        print(' ' * indent + dir)
        print_tree(node[dir], indent + 1)

n = int(input())
root = {}
for _ in range(n):
    path = input().split('\\')
    insert(root, path)
print_tree(root)