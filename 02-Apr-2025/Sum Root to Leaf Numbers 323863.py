# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def walk(root, total):
            if root == None:
                return 0
            total = (total*10) + root.val
            if not root.right and not root.left:
                return total
            return walk(root.left, total) + walk(root.right, total)
        return walk(root, 0)