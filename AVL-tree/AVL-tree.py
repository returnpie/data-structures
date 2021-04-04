class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_child = None
        self.left_child = None
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
                node.height = max(
                    self.calculate_height(node.left_child),
                    self.calculate_height(node.right_child)
                ) + 1
        # we have to visit the right subtree
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                node.height = max(
                    self.calculate_height(node.left_child),
                    self.calculate_height(node.right_child)
                ) + 1

        self.handle_violation(node)

    def handle_violation(self, node):

        while node is not None:
            node.height = max(
                self.calculate_height(node.left_child),
                self.calculate_height(node.right_child)
            ) + 1
            self.violation_helper(node)
            node = node.parent

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:

            if node.left_child is None and node.right_child is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left_child == node:
                    parent.left_child = None
                if parent is not None and parent.right_child == node:
                    parent.right_child = None

                if parent is None:
                    self.root = None

                del node

                self.handle_violation(parent)

            elif node.left_child is None and node.right_child is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    if parent.rightChild == node:
                        parent.right_child = node.right_child
                else:
                    self.root = node.right_child

                node.right_child.parent = parent
                del node

                self.handle_violation(parent)

            elif node.right_child is None and node.left_child is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    if parent.right_child == node:
                        parent.right_child = node.left_child
                else:
                    self.root = node.left_child

                node.left_child.parent = parent
                del node

                self.handle_violation(parent)

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_child)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node

    def violation_helper(self, node):

        balance = self.calculate_balance(node)

        # OK, we know the tree is left heavy BUT it can be left-right heavy or left-left heavy
        if balance > 1:

            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_child) < 0:
                self.rotate_left(node.left_child)

            # this is the right rotation on grandparent ( if left-left heavy, that's single right rotation is needed
            self.rotate_right(node)

        # OK, we know the tree is right heavy BUT it can be left-right heavy or right-right heavy
        if balance < -1:

            # right - left heavy so we need a right rotation  before left rotation
            if self.calculate_balance(node.right_child) > 0:
                self.rotate_right(node.right_child)

            # left rotation
            self.rotate_left(node)

    def calculate_height(self, node):

        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):

        if node is None:
            return 0

        return self.calculate_height(node.left_child) - self.calculate_height(node.right_child)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        l = ''
        r = ''
        p = ''

        if node.left_child is not None:
            l = node.left_child.data
        else:
            l = 'NULL'

        if node.right_child is not None:
            r = node.right_child.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print("%s left: %s right: %s parent: %s height: %s" %
              (node.data, l, r, p, node.height))

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)

        temp_left_child = node.left_child
        t = temp_left_child.right_child

        temp_left_child.right_child = node
        node.left_child = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_child
        temp_left_child.parent = temp_parent

        if temp_left_child.parent is not None and temp_left_child.parent.left_child == node:
            temp_left_child.parent.left_child = temp_left_child

        if temp_left_child.parent is not None and temp_left_child.parent.right_child == node:
            temp_left_child.parent.right_child = temp_left_child

        if node == self.root:
            self.root = temp_left_child

        node.height = max(self.calculate_height(node.left_child),
                          self.calculate_height(node.right_child)) + 1
        temp_left_child.height = max(self.calculate_height(temp_left_child.left_child),
                                     self.calculate_height(temp_left_child.right_child)) + 1

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)

        temp_right_child = node.right_child
        t = temp_right_child.left_child

        temp_right_child.left_child = node
        node.right_child = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_child
        temp_right_child.parent = temp_parent

        if temp_right_child.parent is not None and temp_right_child.parent.left_child == node:
            temp_right_child.parent.left_child = temp_right_child

        if temp_right_child.parent is not None and temp_right_child.parent.right_child == node:
            temp_right_child.parent.right_child = temp_right_child

        if node == self.root:
            self.root = temp_right_child

        node.height = max(self.calculate_height(node.left_child),
                          self.calculate_height(node.right_child)) + 1
        temp_right_child.height = max(self.calculate_height(temp_right_child.left_child),
                                      self.calculate_height(temp_right_child.right_child)) + 1


avl = AVLTree()
avl.insert(5)
avl.insert(12)
avl.insert(31)
avl.insert(3)
avl.insert(14)
avl.insert(61)
avl.insert(6)
avl.insert(1)
avl.insert(15)
avl.insert(2)
avl.insert(17)
avl.insert(8)
avl.insert(71)
avl.insert(81)
avl.insert(91)

# avl.remove(6)

avl.traverse()
