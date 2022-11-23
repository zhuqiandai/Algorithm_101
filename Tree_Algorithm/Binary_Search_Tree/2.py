""" 2022.11.13
    Binary Tree

"""

from node import Node


class BSTree():
    def __init__(self) -> None:
        self.root = None

    # insert
    def insert(self, node: Node):
        p: Node = None
        r: Node = self.root

        while r is not None:
            p = r
            if node.val > r.val:
                r = r.right
            else:
                r = r.left

        node.parent = p

        if p is None:
            self.root = node
        elif node.val < p.val:
            p.left = node
        else:
            p.right = node

    # transplant use v replace u, in the operation u will be removed
    def transplant(self, u: Node, v: Node):
        # u is the root
        if u.parent is None:
            self.root = v

        # u is left node
        elif u == u.parent.left:
            u.parent.left = v

        # u is right node
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    # delete
    def delete(self, tar: Node):
        if tar.left is None:
            self.transplant(tar, tar.right)
        elif tar.right is None:
            self.transplant(tar, tar.left)
        else:
            min = self.min(tar.right)

            if min.parent != tar:
                self.transplant(min, min.right)
                min.right = tar.right
                min.right.parent = min

            self.transplant(tar, min)
            min.left = tar.left
            min.left.parent = min

    # search
    def serach(self, from_node: Node, val) -> Node:
        while from_node is not None:
            if from_node.val == val:
                return from_node

            if val < from_node.val:
                return self.serach(from_node.left, val)

            if val > from_node.val:
                return self.serach(from_node.right, val)

    # inorder
    def in_trav(self, node: Node):
        if node:
            self.in_trav(node.left)
            print("node:", node.val)
            self.in_trav(node.right)

    # max
    def max(self, from_node: Node) -> Node:
        while from_node.right is not None:
            from_node = from_node.right

        return from_node

    # min
    def min(self, from_node: Node):
        while from_node.left is not None:
            from_node = from_node.left

        return from_node


t = BSTree()

vals = [50, 30, 20, 40, 70, 60, 80]
nodes = []


for item in vals:
    nodes.append(Node(item))

for node in nodes:
    t.insert(node)

t.in_trav(t.root)

print("delete 20 node")
t.delete(nodes[2])
t.in_trav(t.root)

print("delete 30 node")
t.delete(nodes[1])
t.in_trav(t.root)

print("delete 50 node")
t.delete(nodes[0])
t.in_trav(t.root)
