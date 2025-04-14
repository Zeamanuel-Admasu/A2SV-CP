# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(start):
            queue = deque([start])
            value = start.val
            
            while queue:
                node = queue.popleft()
                if value != node.val:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return True
        return bfs(root)
                



        