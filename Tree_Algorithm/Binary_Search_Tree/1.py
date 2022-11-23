# 2022.11.18

from node import Node


class BST(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        n = Node(val)
        p = self.root

        # record pointer as the relative parent
        y = None
        while p is not None:
            y = p
            if n.val > p.val:
                p = p.right
            else:
                p = p.left

        n.parent = y

        if y is None:
            self.root = n
        elif n.val > y.val:
            y.right = n
        else:
            y.left = n

    def iter_insert(self, val):
        # TODO
        pass

    def io_trav(self, node):
        if node is not None:
            self.io_trav(node.left)
            print(node.val)
            self.io_trav(node.right)

    def pre_trav(self, node):
        if node is not None:
            print(node.val)
            self.io_trav(node.left)
            self.io_trav(node.right)

    def search(self, node, k):
        print("search path", node.val)

        if k == node.val:
            return node

        if k > node.val:
            return self.search(node.right, k)
        else:
            return self.search(node.left, k)

    def iter_search(self, node, k):
        # 迭代
        while node is not None and k != node.val:
            print("iter search path", node.val)
            if k > node.val:
                node = node.right
            else:
                node = node.left

        return node

    def minimum(self, node):
        while node.left is not None:
            node = node.left

        return node

    def maximum(self):
        pass

    """_summary_
    """

    def transplant(self, u, v):
        """ case 1 root """
        if u.parent is None:
            self.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        if v is not None:
            v.p = u.p

    def delete(self, node):
        # case1 only one node
        if node.left is None:
            self.transplant(node, node.right)

        elif node.right is None:
            self.transplant(node, node.left)

        else:
            k = self.minimum(node.right)
            if node.val != k:
                pass


tree = BST()

tree.insert(3)
tree.insert(8)
tree.insert(10)
tree.insert(2)
tree.insert(5)
tree.insert(7)
tree.insert(6)

# tree.io_trav(tree.root)
print(tree.root.val)
print(tree.root.left.val)
print(tree.root.right.val)

# node = tree.search(tree.root, 5)
