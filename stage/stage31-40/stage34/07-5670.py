import sys
from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.children = dict()
        self.cnt = 0


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        curr_node.cnt += 1
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.cnt += 1

    def average(self):
        curr_node = self.head
        count = self.head.cnt
        q = deque([])
        for child in curr_node.children:
            q.append(curr_node.children[child])
        while q:
            curr = q.popleft()
            if len(curr.children) > 1:
                for child in curr.children:
                    if child != "\n":
                        q.append(curr.children[child])
                        count += curr.children[child].cnt
            else:
                for child in curr.children:
                    q.append(curr.children[child])
        return count / self.head.cnt


while 1:
    trie = Trie()
    try:
        n = int(sys.stdin.readline())
    except:
        break
    for __ in range(int(n)):
        trie.insert(sys.stdin.readline())
    print("%.2f" % trie.average())
