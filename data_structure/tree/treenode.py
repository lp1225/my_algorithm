# 简单二叉树结构
from queue import Queue


class  TreeNode(object):
    """二叉树"""
    def __init__(self, data):
        self.data = data # 节点数
        self.node_left = None
        self.node_right = None


def preorder(node):
    """先序遍历
        根左右
    """
    if node != None:
        print(node.data, end= '')
        preorder(node.node_left)
        preorder(node.node_right)


def inorder(node):
    """中序遍历
       左根右
    """
    if node != None:
        inorder(node.node_left)
        print(node.data, end='')
        inorder(node.node_right)


def postorder(node):
    """后序遍历
       左右根
    """
    if node != None:
        postorder(node.node_left)
        postorder(node.node_right)
        print(node.data, end='')


def comorder(node):
    """层序遍历， 广度优先搜索bfs
       通过队列来实现
    """
    q = Queue()
    q.put(node)
    if node.data != None:
        # 循环取出node
        while q.empty() != True:
            node = q.get(0)
            print(node.data, end='')
            if node.node_left:
                q.put(node.node_left)
            if node.node_right:
                q.put(node.node_right)
       
if __name__ == '__main__':
    n1 = TreeNode(5)
    n2 = TreeNode(6)
    n3 = TreeNode(7)
    n4 = TreeNode(8)

    n1.node_left = n2
    n1.node_right = n3
    n2.node_left = n4

    # print(n1.node_left.data)
    # print(n4.node_right)
    # print('-----------------')
    # preorder(n1)
    # print('')
    # inorder(n1)
    # print('')
    # postorder(n1)
    comorder(n1)

