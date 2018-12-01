# 定义一个链表


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist(object):

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """加入数据"""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # 向下走一步
            self.tail.next = node
            self.tail = node
    
    def is_empty(self):
        return self.head is None
    
    def insert(self, idx, value):
        """需要知道上一个节点的信息"""
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node
            
    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def search(self):
        """查询数据"""
        pass


if __name__ == '__main__':
    list = Linklist()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    list.append(node1)
    list.append(node2)
    list.append(node3)
    list.append(node4)

    for i in list.iter():
        print(i)
