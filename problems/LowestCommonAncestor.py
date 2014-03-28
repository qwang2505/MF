'''
Created on: Mar 28, 2014

@author: qwang

An implementation of an algorithm to find the least common ancestor of two
values in a binary search tree.

In a tree structure, an ancestor of a node v is a node u that is on the
path from v back up to the root of the tree.  (Note that this includes the
node v itself, which might be a bit confusing since a person is typically
not considered to be her own ancestor!)  A common ancestor of two nodes v1
and v2 in a tree is a node u that is an ancestor of both v1 and v2. Finally,
if v1 and v2 have any common ancestors, then they must have a lowest
common ancestor (LCA), which is the common ancestor as deep in the tree as
possible.

The LCA problem has been well-studied and several very fast algorithms exist
that allow LCA queries to be executed efficiently after a small amount of
preprocessing on the tree.

This file contains a function for determining the least common ancestor of
two nodes that are in the same binary search tree.  The algorithm runs in
time O(h), where h is the height of the tree, and uses only O(1) space.

To motivate the solution, let's consider the following BST:

                7
              /  \
             /    \
            /      \
           /        \
          2         12
         / \        / \
        1   5      9  13
           / \    / \   \
          4   6  8  11  15
         /          /   / \
        3          10  14 16 


(Sorry for the gap near the root!)  Let's suppose that we want to find the
LCA of the nodes 8 and 10, which is 9.  How might we determine this?  One
simple way to do this would be do a standard BST lookup on 8 and on 10,
storing all of the nodes found on the access path from the root, and then
find the last node that these lists have in common.  This approach would use
O(h) time and O(h) space, where h is the height of the tree.

However, it's not actually necessary to store the full access paths to 8 and
to 10.  Specifically, we can make the following observation.  We know that
when we start our search at the root, as long as we know that 8 and 10 are
actually nodes in the BST, that the root has to be one of their common 
ancestors.  Since 7 < 8 and 7 < 10, we know that both 8 and 10 must be in
the right subtree (if they're in the tree at all).  Therefore, the root of
the right subtree is also a common ancestor of 8 and 10, so the tree root
cannot be their LCA.  Consequently, we can recursively search the right
subtree to get the LCA of the two nodes.

At node 12, we can similarly realize that 8 < 12 and 10 < 12, so 8 and 10,
if they exist in the tree at all, and so the root of the left subtree would
be a lower common ancestor of 8 and 10 (if these values are even in the tree
at all).  Therefore, we can recurse on the left subtree.

This brings us to node 9.  Here, we note that 8 < 9 and 9 < 10, meaning that
8 belongs to the left subtree and 10 belongs to the right subtree.  This
means that no ancestor of 10 can be in the left subtree and no ancestor of
8 can be in the right subtree.  Accordingly, there can be no common
ancestors of 8 and 10 below the current node of 9.  Therefore, as long as 8
and 10 actually appear anywhere in the BST, we are guaranteed that 9 has to
be their LCA.

Under the assumption that v1 and v2 are values that actually appear in the
BST rooted at r, we therefore have the following core logic:

    If v1 and v2 are on the same side as r, recurse into that side.
    If v1 and v2 are on different sides of r, r is their LCA.
    If r has value v1 or v2, r is their LCA.

(That last step didn't appear during the above algorithm trace, but for
completeness it's important to include it!)

The above algorithm traces a path down the BST, and therefore has time
complexity at most O(log n).  Additionally, it only uses O(1) storage space.
However, the algorithm does assume that the values v1 and v2 actually
appear in the tree.  If they do not, then we need to modify the above
algorithm so that upon finding a node that would be the LCA of the two nodes
if they actually appear in the tree, we do a secondary test to make sure
that the nodes actually appear in the BST at all.
'''

class LowestCommonAncestor(object):
    '''
    Implementation of finding lowest common ancestor of binary search tree.
    '''

    @classmethod
    def find(cls, tree, first_value, second_value):
        '''
        Find lowest common ancestor of the given binary search tree
        '''
        # TODO valid values, must not equal and in tree
        if first_value < second_value:
            return cls._find(tree.root, first_value, second_value)
        else:
            return cls._find(tree.root, second_value, first_value)

    @classmethod
    def _find(cls, node, first_value, second_value):
        '''
        Find lowest common ancestor of the given sub tree.
        NOTICE first value must lower than second value
        '''
        if node.value > second_value:
            return cls._find(node.left, first_value, second_value)
        elif node.value < first_value:
            return cls._find(node.right, first_value, second_value)
        else:
            return node

if __name__ == '__main__':
    import sys
    sys.path.append('../')

    from common.BST import BST

    # create binary search tree
    bst = BST([7, 2, 1, 5, 4, 3, 6, 12, 9, 13, 8, 11, 10, 15, 14, 16])
    _node = LowestCommonAncestor.find(bst, 3, 6)
    print _node.value
