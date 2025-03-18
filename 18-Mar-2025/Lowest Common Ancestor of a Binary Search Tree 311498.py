# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = min(p.val, q.val)
        b = max(p.val, q.val)
        
        
        while root:
            if root.val >= a and root.val <= b:
                return root
            elif root.val > a and root.val > b:
                root = root.left
            else:
                root = root.right 
        