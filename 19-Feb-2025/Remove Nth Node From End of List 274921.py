# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        count = 0
        curr = dummy
        while curr.next:
            curr = curr.next
            count += 1
        print(dummy.next)
        target = count - n

        curr = dummy
        count2 = 0
        while count2 < target:
            curr = curr.next
            count2 += 1
        
        curr.next = curr.next.next
        curr = curr.next
        return dummy.next
        