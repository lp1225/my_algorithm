# 搜索二叉树
from queue import Queue


class Node(object):
    """节点"""
    def __init__(self, data):
        self.data = data
        self.node_left = None
        self.node_right = None

class BinaryTree(object):
    
    def __init__(self):
        self.root = None
    
def insert(tree, node):
    """插入节点"""
    if tree.root == None:
        tree.root = node
    else:
        temp = tree.root # 必须要有一个临时节点
        while temp != None:
            if temp.data > node.data:
                if temp.node_left == None:
                    temp.node_left = node
                    return
                else:
                    temp = temp.node_left
            else:
                if temp.node_right == None:
                    temp.node_right = node
                    return
                else:
                    temp = temp.node_right

def preorder(node):
    """先序遍历"""
    if node != None:
        print(node.data, end='')
        preorder(node.node_left)
        preorder(node.node_right)

def inorder(node):
    """中序遍历"""
    if node != None:
        inorder(node.node_left)
        print(node.data, end='')
        inorder(node.node_right)

def postorder(node):
    """后序遍历"""
    if node != None:
        postorder(node.node_left)
        postorder(node.node_right)
        print(node.data, end='')

def get_height(node):
    """得到最大高度k"""
    if node == None:
        return 0
    max_left = get_height(node.node_left)
    max_right = get_height(node.node_right)
    max_value = max(max_left, max_right)
    return max_value+1

def get_node(node, k):
    """得到k层的节点"""
    if node == None:
        return
    if k == 1:
        if node.data !=None:
            print(node.data, end='')
    get_node(node.node_left, k-1)
    get_node(node.node_right, k-1)

def get_max(node):
    """查找最大值
       在右子树中找
    """
    if node != None:
        while node.node_right != None:
            node = node.node_right

    return node.data
def get_min(node):
    """查找最小值"""
    if node != None:
        while node.node_left != None:
            node = node.node_left
    return node.data

def comorder(node):
    q = Queue()
    q.put(node)
    if node == None:
        return
    else:
        while q.empty() != True:
            node = q.get(0)
            print(node.data, end='')
            if node.node_left != None:
                q.put(node.node_left)
            if node.node_right != None:
                q.put(node.node_right)


def Mirror(node):
    """反转二叉树，
       顺序执行,nice
    """
    if node == None:
        return
    if node.node_left == None and node.node_right == None:
        return
    temp = node.node_left
    node.node_left = node.node_right
    node.node_right = temp

    Mirror(node.node_left)
    Mirror(node.node_right)

if __name__ == '__main__':
    tree = BinaryTree()
    arr_test = [6, 3, 8, 2, 5, 1, 7]
    for i in arr_test:
        insert(tree, Node(i))
    # preorder(tree.root)
    # print()
    # inorder(tree.root)
    # print()
    # get_node(tree.root, 3)
    # print()
    # result = get_height(tree.root)
    # print(result)
    # max_value = get_max(tree.root)
    # print(max_value)
    # min_value = get_min(tree.root)
    # print(min_value)
    comorder(tree.root)
    Mirror(tree.root)
    print()
    comorder(tree.root)

        
