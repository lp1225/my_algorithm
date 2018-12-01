# 定义一个HashTable

num = 10

# 设置一个节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def data_equals(self, data):
        return self.data == data


class HashTable(object):
    """HashTable"""
    # 确定结构， 确定功能insert，search，delete， 确定散列规则
    # 数组和链表的结合, 数据存在节点中
    def __init__(self):
        self.value = [None]*num

    def insert(self, data):
        """插入数据"""
        index = data % num
        node = Node(data)
        if self.value[index] is None:
            self.value[index] = node
            return True
        else:
            head = self.value[index]
            # 遍历节点去链接
            while head.get_next() is not None:
                head = head.get_next()
            head.set_next(node)
            return True

    def search(self, data):
        """查找数据"""
        # index = data % num
        # head = self.value[index]
        # if head is None:
        #     return False
        # else:
        #     while head and not head.get_next().data_equals(data):
        #         head = head.get_next()
        #     if head:
        #         return head.data
        #     else:
        #         return False
        i = data % num
        if self.value[i] is None:
            return False
        else:
            head = self.value[i]
            while head and not head.data_equals(data):
                head = head.get_next()
            if head:
                return head
            else:
                return False

    def delete(self, data):
        """删除数据"""
        result = self.search(data)
        if result is False:
            print('不存在这个数据')
            return False
        else:
            index = data % num
            head = self.value[index]
            while not head.get_next().data_equals(data):
                head = head.get_next()
            # head.set_next(head.get_next().get_next()) # 节点指向None
            head.next_node = None
            
            return True


if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.insert(10)
    hashTable.insert(11)
    hashTable.insert(1)
    # print(hashTable.value)
    print(hashTable.search(1))
    print(hashTable.delete(1))
    print(hashTable.value)
    print(hashTable.search(10))
