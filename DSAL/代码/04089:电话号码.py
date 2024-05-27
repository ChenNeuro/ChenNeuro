class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def is_prefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            elif node.children[char].end_of_word:
                return True
            node = node.children[char]
        return False


t = int(input())
for _ in range(t):
    n = int(input())
    phone_numbers = [input() for _ in range(n)]
    phone_numbers.sort()
    trie = Trie()
    consistent = True

    for phone in phone_numbers:
        if trie.is_prefix(phone):
            consistent = False
            break
        trie.insert(phone)
    if consistent:
        print("YES")
    else:
        print("NO")