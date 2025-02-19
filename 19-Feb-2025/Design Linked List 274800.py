# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0

    def get(self, index: int) -> int:
        dummy = ListNode()
        dummy.next = self.head
        curr = dummy.next
        i = 0
        while curr:
            if i != index:
                i += 1
                curr = curr.next
            else:
                return curr.val
        return -1
    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        if index < 0 or index > self.size: 
            return
        if index == 0:
            self.addAtHead(val)
            return 
        if index == self.size:
            self.addAtTail(val)
            return
        dummy = ListNode()
        dummy.next = self.head
        curr = dummy
        count = 0
        while count < index:
            curr = curr.next
            count += 1
        
        newNode.next = curr.next
        curr.next = newNode

        self.size += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)