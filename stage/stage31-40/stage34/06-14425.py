import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True


trie = Trie()
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    tmp = list(sys.stdin.readline())
    trie.insert(tmp)
cnt = 0
for _ in range(m):
    tmp = list(sys.stdin.readline())
    if trie.search(tmp):
        cnt += 1
print(cnt)