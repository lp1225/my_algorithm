# 测试 trie


class Node(object):

    def __init__(self):
        self.value = None
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        word = word.lower()
        node = self.root
        for char in word:
            if char not in node.children:
                # 创建
                child = Node()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = word
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node.value


if __name__ == '__main__':
    trie = Trie()
    trie.insert('hello')
    trie.insert('nice')
    trie.insert('to')
    trie.insert('meet')
    trie.insert('you')
    print(trie.search('h'))
    print(trie.search('hello'))

    
