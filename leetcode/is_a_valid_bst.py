"""
Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(root):
    # Tree schema
    # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def create_tree1(_root):
    # Tree schema
    # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    _root = TreeNode(3)
    _root.left = TreeNode(2)
    _root.right = TreeNode(5)
    _root.left.left = TreeNode(1)
    _root.left.right = TreeNode(4)
    return _root


def in_order_traversal(_root):

    if _root is None:
        return
    in_order_traversal(_root.left)
    print(f"{_root.val}", end=" ")
    in_order_traversal(_root.right)


def post_order_traversal(_root):
    """ Reverse sort """
    if _root is None:
        return
    post_order_traversal(_root.left)
    post_order_traversal(_root.right)
    print(f"{_root.val}",end=" ")


#Driver code
root = None
root = create_tree1(root)
print("in order:")
in_order_traversal(root)
print()
print("post order:")
post_order_traversal(root)
