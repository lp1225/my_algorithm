# python 字典模拟node实现前缀树


class Trie(object):
    def __init__(self):
        self.root = {}
        self.END = '/'

    def add(self, word):
        # 遍历单词，添加
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.END in node


if __name__ == '__main__':
    str1 = 'to'
    str2 = 'tea'
    str3 = 'ted'
    str4 = 'ten'
    str5 = 'inn'
    list_str = [str1, str2, str3, str4, str5]
    trie = Trie()
    for i in list_str:
        trie.add(i)
    result = trie.find('t')
    print(result)
    print(trie.root)
