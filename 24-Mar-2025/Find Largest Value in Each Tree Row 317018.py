# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = 0
        count = 0
        queue = deque([(root, level)])
        res = []
        final = []
        while queue:
            node, count = queue.popleft()
            if level != count:
                final.append(max(res))
                level += 1
                res = []
            res.append(node.val)
            if node.left:
                queue.append((node.left, count+1))
            if node.right:
                queue.append((node.right, count+1))
        final.append(max(res))
        return final


        