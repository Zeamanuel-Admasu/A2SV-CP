# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def helper(node, val):
            if node == None:
                return None
            if node.val > val:
                return helper(node.left, val)
            elif node.val == val:
                print("aa", node)
                return node
            else:
                return helper(node.right, val)
        return helper(root, val)


        