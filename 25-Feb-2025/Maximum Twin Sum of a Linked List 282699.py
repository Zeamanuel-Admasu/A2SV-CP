# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        self.head = head
        arr = []
        while self.head:
            arr.append(self.head.val)
            self.head = self.head.next
        i = 0
        j = len(arr) - 1
        summ = 0
        while i < j:
            summ = max(summ, (arr[i] + arr[j]))
            i += 1
            j -= 1
        return summ


        print(arr)
        return 1
        