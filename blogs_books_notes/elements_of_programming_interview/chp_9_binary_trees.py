""" Chapter 9. Binary Trees"""

"""

Root, left, right.
A node is an ancestor of d if it lies on the search path from the root ot d. If a node is an ancestor of d, we say d is 
    a descendant of that node.

Leaf: node that has no descendants
depth: depth of a node is the number of nodes on the search path from the root to n, not including n itself
height: max depth of any node in the tree
level: level of a tree is all nodes at the same depth

full binary tree: BT in which every node other than the leaves has two children 
perfect binary tree: a tree that has all leaves at the same depth, and every parent with two children

traversal methods:

inorder: traverse the left subtree, visit the root, then traverse the right subtree
preorder: visit the root, traverse the left subtree, then traverse the right subtree
postorder: traverse the left subtree, traverse the right subtree, then visit the root

O(n) time and O(h) additional space complexity. If a node has a parent field, the traversal can be done with O(1) 
    additional space complexity.

 
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


ex_tree = BinaryTreeNode(314)
ex_tree.left = BinaryTreeNode(6,
                              BinaryTreeNode(271,
                                             BinaryTreeNode(28),
                                             BinaryTreeNode(0)
                                             ),
                              BinaryTreeNode(561,
                                             None,
                                             BinaryTreeNode(3,
                                                            BinaryTreeNode(17)
                                                            )
                                             )
                              )
ex_tree.right = BinaryTreeNode(6,
                               BinaryTreeNode(2,
                                              None,
                                              BinaryTreeNode(1,
                                                             BinaryTreeNode(401,
                                                                            None,
                                                                            BinaryTreeNode(641)),
                                                             BinaryTreeNode(257)
                                                             )),
                               BinaryTreeNode(271,
                                              None,
                                              BinaryTreeNode(28))
                               )



def tree_traversal(root: BinaryTreeNode) -> None:
    if root:
        # preorder: process the root before the traversals of left and right children
        # postorder: left subtree, right subtree, root
        # inorder: left subtree, root, right subtree
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)
        print('Inorder: %d' % root.data)
        tree_traversal(root.right)
        print('Postorder: %d' % root.data)


"""
Time complexity of each approach is O(n) - where n is the # of nodes in the tree.

* Recursive algorithms are well-suited to problems on trees. Remember to include space implicitly allocated on the 
    function call stack when doing space complexity analysis.  

* Brute force usually uses O(n) space. What you want is O(1) usually.

* Consider left- and right-skewed trees when doing complexity analsis. Note that O(h) complexity, where h is the tree
    height, translates to O(logn) complexity for balanced trees, but O(n) For skewed trees.
    
* If each node has a parent field, use it to make your code simpler, and to reduce time and space complexity.

* It's easy to make the mistake of treating a node that has a single child as a leaf. 
"""


"""
9.1. Test if a binary tree is height-balanced

A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of its left
    and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete binary tree. A
    height-balanced binary tree does not have to be perfect or complete.

Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced.

Hint: Think of a classic binary tree algorithm.

"""
import collections

t2 = BinaryTreeNode(6, BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(1)),
                    BinaryTreeNode(561, None, BinaryTreeNode(3, BinaryTreeNode(10))))

t3 = BinaryTreeNode(6,
                    BinaryTreeNode(2, BinaryTreeNode(1, BinaryTreeNode(1)),BinaryTreeNode(1,BinaryTreeNode(401),
                                                          BinaryTreeNode(257))),
                    BinaryTreeNode(271,None,BinaryTreeNode(28)))


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    if tree.right is None and tree.left is None:
        return True
    elif tree.right is None:
        return tree.left is not None and (tree.left.left is None and tree.left.right is None)
    elif tree.left is None:
        return tree.right is not None and (tree.right.left is None and tree.right.right is None)
    elif is_balanced_binary_tree(tree.left) and is_balanced_binary_tree(tree.right):
        return True
    else:
        return False


def is_bal_bin_tree_recursive(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )
    def check_balance(tree: BinaryTreeNode):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        left_tree = check_balance(tree.left)
        if not left_tree.balanced:
            return BalancedStatusWithHeight(False, 0)
        right_tree = check_balance(tree.right)
        if not right_tree.balanced:
            return BalancedStatusWithHeight(False, 0)

        balanced = abs(left_tree.height - right_tree.height) < 2
        height = max(left_tree.height, right_tree.height) + 1
        return BalancedStatusWithHeight(balanced, height)
    return check_balance(tree).balanced


"""
9.4. Compute the LCA when nodes have parent pointers

Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that each node has a parent 
    pointer.
Hint: The problem is easy if both nodes are the same distance from the root.


"""