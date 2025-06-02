# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        res = []
        final = []
        count1 = 0
        if not root:
            return 0
        queue = deque([(root, level)])
        while queue:
            node, count = queue.popleft()
            if count != level:
                count1 += 1
                level = count
                final.append(res)
                res = []
            res.append((node, count))
            if node.left:
                queue.append((node.left, count + 1))
            if node.right:
                queue.append((node.right, count + 1))
        count1 += 1
        return count1

        