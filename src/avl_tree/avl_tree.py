class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

    def get_height(self, node):
        return 1
