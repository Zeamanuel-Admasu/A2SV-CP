# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        res = []
        final = []
        level = 0
        queue = deque([(root, level)])
        while queue:
            node,count = queue.popleft()
            if level != count:
                final.append(res)
                level = count
                res = []
            res.append(node.val)

            if node.left != None:
                queue.append((node.left, count + 1))
            if node.right != None:
                queue.append((node.right, count + 1))
        
        final.append(res)
        return final


        