# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr1 = []
        i = 0
        while len(arr) - i >= k:
            arr1.extend(arr[i:i + k][::-1])
            i += k
        if i < len(arr):
            for j in range(i, len(arr)):
                arr1.append(arr[j])
        dummy = ListNode(0)
        current = dummy
        for val in arr1:
            current.next = ListNode(val)
            current = current.next

        return dummy.next



        