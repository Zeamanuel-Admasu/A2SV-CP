# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        arr = []
        while self.head:
            arr.append(self.head.val)
            self.head = self.head.next
        odd = []
        even = []
        for i in range(len(arr)):
            if i % 2 == 0:
                even.append(arr[i])
            else:
                odd.append(arr[i])
        arr = even + odd
        print(arr)
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return dummy.next




               