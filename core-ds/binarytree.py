from treenode import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value: int):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return
        cur_node = self.root
        while True:
            if value >= cur_node.value:
                if cur_node.right is None:
                    cur_node.right = node
                    return
                cur_node = cur_node.right
            else:
                if cur_node.left is None:
                    cur_node.left = node
                    return
                cur_node = cur_node.left

    def inorder_traversal(self, node: TreeNode):
        if not node:
            return
        self.inorder_traversal(node.left)
        print(node.value, end=" ")
        self.inorder_traversal(node.right)