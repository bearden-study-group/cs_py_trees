class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            # go left
            if self.left is not None:
                # we have a left child
                # let the left child deal with the new value
                self.left.insert(new_value)  # recursion
            # we do NOT have a left child
            else:
                # since we don't have a left child,
                # we'll make this value a Node, and make it our
                # new left child
                self.left = BSTNode(new_value)
        else:
            # new_val is LARGER THAN
            # OR EQUAL TO self.value
            # so go right
            if self.right is not None:  # if our right child exists
                # let the right child deal with new_value
                self.right.insert(new_value)
            else:  # our right child does NOT exist (or, is None)
                # so make a node with new_value
                # and make that new node our right child
                self.right = BSTNode(new_value)

    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    def get_min(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value


if __name__ == '__main__':
    bst = BSTNode(8)
    bst.insert(2)
    bst.insert(10)
    bst.insert(40)
    max_val = bst.get_max()
    min_val = bst.get_min()
    print(max_val)  # 40
    print(min_val)  # 2
