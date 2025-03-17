# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def helper(node, val, par):
            if node == None:
                return par
            if node.val < val:
                return helper(node.right, val, node)
            elif node.val > val:
                return helper(node.left, val, node)
            # elif node.val == val:
            #     return self.root
        par = helper(root, val, None)
        new_node = TreeNode(val)
        if par.val < val:
            par.right = new_node
        else:
            par.left = new_node
        return root
        
        