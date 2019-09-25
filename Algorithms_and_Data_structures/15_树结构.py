class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data


class BinTree:
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_form(cls, node_list):
        '''
        通过节点信息构造二叉树
        第一遍遍历创建节点
        第二遍遍历给root 和子节点赋值
        最后用root初始化类返回一个对象
        :param node_list: [{'data':'A','left':'B','right':'C','is_root':False},{},{},...]
        :return:
        '''
        node_dict = {}  # 创建字典对储存每个node
        for node_data in node_list:  # 遍历数据集
            data = node_data['data']  # data = A
            node_dict[data] = Node(data)  # 在字典node_dict中 key:data , value : node
        for node_data in node_list:  # 再一次遍历数据集
            data = node_data['data']  # 取出要处理的节点名称
            node = node_dict[data]  # 从node_dict中通过key取出保存的node对象
            if node_data['is_root']:  # 判断 是否为root 爸爸节点
                root = node
            node.left = node_data.get(node_data['left']) # 如果不是root节点 则对其left属性赋值，值为数据集中的left
            node.right = node_data.get(node_data['right'])
        return cls(root)

    def preorder_trav(self, subtree):
        '''
        先(根)序遍历
        :param subtree:
        :return:
        '''
        if subtree is not None:
            print(subtree.data)  # 递归函数里先处理根
            self.preorder_trav(subtree.left)  # 递归处理左子树
            self.preorder_trav(subtree.right)  # 递归处理右子树


if __name__ == '__main__':
    node_list = [
        {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False},
    ]
    btree = BinTree.build_form(node_list)
    btree.preorder_trav(btree.root)
