# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        def helper(node):
            
            if not node:
                return None
            
            node.next = helper(node.next)

            if node.val == val:
                return node.next
            return node
        return helper(head) 

        