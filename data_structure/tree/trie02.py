# 前缀树


class Node(object):
    def __init__(self):
        self.value = None
        self.children = {}   # 结构为{'a':node}


class Trie(object):
    def __init__(self):
        self.root = Node()  # 前缀树根节点为空
    
    def insert(self, word):
        """插入节点
           不存在则创建节点
        """
        # key should be a low-case string, this must be checked here!
        node = self.root
        for char in word:
            if char not in node.children:
                child = Node()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = word

    def insert02(self, word):
        """插入节点
           不存在则创建节点
        """
        # key should be a low-case string, this must be checked here!
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                child = Node()
                node.children[word[i]] = child
                node.value = word[:i]
                node = child
            else:
                node = node.children[word[i]]
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
    # trie = Trie()
    # trie.insert('hello')
    # trie.insert('nice')
    # trie.insert('to')
    # trie.insert('meet')
    # trie.insert('you')
    # print(trie.search('h'))
    # print (trie.search('hello'))
    trie = Trie()
    trie.insert02('hello')
    trie.insert02('nice')
    trie.insert02('to')
    trie.insert02('meet')
    trie.insert02('you')
    print(trie.search('h'))
    print(trie.search('hello'))
    print(trie.search('mee'))
            
