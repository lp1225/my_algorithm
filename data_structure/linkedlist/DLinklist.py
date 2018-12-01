# 双向链表


class Node(object):
    """双向链表的节点"""
    def __init__(self, item):
        self.item = item
        self. next = None
        self. prev = None

class DLinklist(object):
    """双向链表"""
    def __init__(self):
        self.__head = None
    
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None
    
    def length(self):
        """返回链表的长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
    
    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # node的next指向__head的头节点
            node.next = self.__head
            # 将__head的头节点的prev指向node
            self.__head.prev = node
            self.__head = node
    
    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur
    
    def search(self, item):
        """查找元素是否存在"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            # 移动到指定位置前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            node.next = cur.next

            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        """删除元素"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                    # 如果存在下一个节点，则设置下一个节点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 如果存在下一个节点，则设置下一个节点
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

if __name__ == '__main__':
    ll = DLinklist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(4))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
