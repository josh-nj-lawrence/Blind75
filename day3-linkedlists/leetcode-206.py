# Reverse Linked List #206
# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=None, next=None):
        self.val = val 
        self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head # Set current node to head
            head = head.next # Move Head
            curr.next = prev # Set next node to previous
            prev = curr
        return prev

l3 = ListNode(1)
l2 = ListNode(2, l3)
l1 = ListNode(3, l2)

solution = Solution()
solution.reverseList(l1)


    