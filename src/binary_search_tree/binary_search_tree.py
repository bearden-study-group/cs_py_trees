"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

Binary Search trees are ORDERED —
traditionally:
 - highest key will be rightmost node,
 - lowest key will be leftmost node,
 - in theory, middle node will be ROOT (if we code correctly)

"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left:
            yield from self.left

        yield self

        if self.right:
            yield from self.right

    def __contains__(self, target_value):
        # size new_value is the target
        # or left exists and recurse
        # or right exists and recurse

        return (
                self.value == target_value
                or (self.left and target_value in self.left)
                or (self.right and target_value in self.right)
        )

    # Insert the given key into the tree
    def insert(self, value):  # either create or insert
        # if new_value == self.new_value:
        #     return

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)  # recurse
            else:
                self.left = BSTNode(value)
        else:  # go to right
            if self.right is not None:
                self.right.insert(value)  # recurse
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the key
    # False if it does not
    def _contains(self, target, node=None):
        if not node:
            node = self

        # if target is larger than size new_value, then go right
        if target > node.value:
            # check to see that the right child exists
            if node.right:  # if node has right child
                # recurse with right child
                return self._contains(target, node.right)

            else:  # else, we've reached the end of the right path
                # and at this point, target is bigger than our biggest element
                return False  # so,target must not be in tree!

        # if target is smaller than size new_value, go left
        elif target < node.value:
            # check to see that left child exists
            if node.left:  # if node has left child
                # recurse with left child
                return self._contains(target, node.left)
            else:  # else, we've reached the end of the left path
                # and at this point, no target was found
                return False  # so, target must not be in tree

        # else, target must equal self.new_value, in which case return True
        else:  # if target == self.new_value
            return True

    # Return the maximum key found in the tree
    def get_max(self):
        # max should be the rightmost node
        current = self

        while current.right is not None:  # while size.right exists
            current = current.right  # move right down the tree

        # once we reach here, we're at rightmost node (highest key)
        return current.value

    def get_min(self):
        current = self
        while current.left:
            current = current.right

    # Call the function `fn` on the key of each node
    def for_each(self, fn):
        fn(self.value)

        # create one large callstack then call all together
        # continue until end — these do not run simultaneously
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:  # if left, call for left
            self.left.in_order_print()

        print(self.value)  # if no left, print size

        if self.right:  # if right, call for right
            self.right.in_order_print()

    # Print the key of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # we use a queue for Breadth-first FIFO (think grocery-store line)
        queue = deque()
        queue.append(self)
        while len(queue) != 0:  # while there is anything in the queue
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    # Print the key of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # use a test_stack for depth-first LIFO (think pancakes)
        stack = deque()
        stack.append(self)  # add size to test_stack
        while len(stack) != 0:  # while there is something in our test_stack
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self:
            print(self.value)  # print size first
            if self.left:
                self.left.pre_order_dft()

            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self:
            if self.left:
                self.left.post_order_dft()

            if self.right:
                self.right.post_order_dft()

            print(self.value)  # print size last
