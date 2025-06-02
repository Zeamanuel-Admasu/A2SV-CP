# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        if not root:
            return []
        queue = deque([(root, level)])
        res = []
        final = []
        while queue:
            node, count = queue.popleft()
            if count != level:
                if level % 2 == 1:
                    res.reverse()
                final.append(res)   
                level = count
                res = []
            res.append(node.val)
            if node.left:
                queue.append((node.left, count + 1))
            if node.right:
                queue.append((node.right, count + 1))
        if level % 2 == 1:
            res.reverse()
        final.append(res)
        return final



        