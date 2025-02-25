# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        self.head1 = l1
        self.head2 = l2
        while self.head1:
            list1.append(self.head1.val)
            self.head1 =self.head1.next
        while self.head2:
            list2.append(self.head2.val)
            self.head2 =self.head2.next
        list1 = list1[::-1]
        list2 = list2[::-1]
        intval1 = 0
        intval2 = 0
        for num in list1:
            intval1 = intval1 * 10 + num
        for num in list2:
            intval2 = intval2 * 10 + num


        summ = intval1 + intval2
        arr = [int(digit) for digit in str(summ)]
        arr = arr[::-1]
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head           