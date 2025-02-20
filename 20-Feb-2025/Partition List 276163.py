# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        arr1 = []
        while curr and curr.next:
            curr = curr.next
            arr1.append(curr.val)
        target = []
        for elem in arr1:
            if elem < x:
                target.append(elem)

        arr1 = list(filter(lambda x: x not in target, arr1))
        final = target + arr1
        
        if len(final) == 0:
            return 
        head = ListNode(final[0])
        current = head
        for elem in final[1:]:
            current.next = ListNode(elem)
            current = current.next

        return head


        