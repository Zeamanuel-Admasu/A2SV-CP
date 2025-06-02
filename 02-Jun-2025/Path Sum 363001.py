# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        level = root.val
        res = []
        final = []
        some = []
        
        queue = deque([(root, level)])
        while queue:
            node, count = queue.popleft()
            
            if not node.left and not node.right:
                if count == targetSum:
                    return True
            if node.left:
                queue.append((node.left, count + node.left.val))
            if node.right:
                queue.append((node.right, count + node.right.val))
        return False
        
        