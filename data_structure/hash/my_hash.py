# 生成简单的hash表
# 结构[(,)]

class MyHash(object):
    """myhash"""

    def __init__(self):
        self.value = []
    
    def insert(self, k, v):
        # 直接加入
        self.value.append((k, v))
    
    def search(self, k):
        """提供查询功能"""
        for key, value in self.value:
            if k == key:
                return value
        raise KeyError 


if __name__ == '__main__':
    hash = MyHash()
    hash.insert('a', '1')
    hash.insert('b', '2')
    result = hash.search('b')
    print(result)          
            
