# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_Successor(node):
            if node.left == None:
                return node
            return find_Successor(node.left)
        if root == None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)    
        else:
            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            temp = find_Successor(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root
          