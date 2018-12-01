# Binary Search Tree 二叉搜索树


class Node(object):

    def __init__(self, data):
        self.data = data
        self.node_left = None
        self.node_right= None


class Tree(object):
    
    def __init__(self):
        self.root = None


def insert(tree, value):
    """插入数据，组成二叉搜索树"""
    # 创建起始节点
    node = Node(value)
    if tree.root == None:
        tree.root = node
    else:
        temp = tree.root #当前比较的节点
        while temp != None:
            if value < temp.data:
                # 走左边
                if temp.node_left == None:
                    temp.node_left = node
                    return
                else:
                    temp = temp.node_left
            else:
                # 走右边
                if temp.node_right == None:
                    temp.node_right = node
                    return
                else:
                    temp = temp.node_right


def preorder(node):
    """先序遍历
        根左右
    """
    if node != None:
        print(node.data, end='')
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


def get_height(node):
    if node == None:
        return 0
    else:
        left_h = get_height(node.node_left)
        right_h = get_height(node.node_right)
        max_value = max(left_h, right_h)
        # max_value = left_h
        # if right_h > max_value:
        #     max_value = right_h
        return max_value+1


def get_level(node, k):
    """打印出第k层的节点个数"""
    if node == None or k < 1:
        return 0
    if k == 1:
        return 1
    nums_left = get_level(node.node_left, k-1)
    nums_right = get_level(node.node_right, k-1)
    return nums_left+nums_right


def get_node(node, k):
    """打印出k层所有节点"""
    if k == 1:
        if node !=None:
            print(node.data)
        return
    nums_left = get_node(node.node_left, k-1)
    nums_right = get_node(node.node_right, k-1)

if __name__ == '__main__':
    arr_test = [6, 3, 8, 2, 5, 1, 7]
    tree = Tree()
    for i in arr_test:
        insert(tree, i)
    # preorder(tree.root)
    # print('')
    # inorder(tree.root)
    # value = get_height(tree.root)
    # print(value)
    # postorder(tree.root)
    # level = get_level(tree.root, 4)
    # print(level)

    get_node(tree.root, 3)
