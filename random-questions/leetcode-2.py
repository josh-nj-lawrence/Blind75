# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

from typing import List, Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "",""
        head1, head2 = l1.val, l2.val
        while head1 != None and head2 != None:
            l1 += str(head1)
            l2 += str(head2)
            head1, head2 = l1.next.val, l1.next.val
        if next == None:
            pass
            # Not done

class Solution2:  # Time: O(n) and Space: O(n)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()  # Creating a new node to store l1 + l2 values, dummy will give us head address & cur will be used to append new nodes
        carry = 0

        while l1 or l2 or carry:  # we will continue till either one of these have positive values left 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Addition: New digits
            val = v1 + v2 + carry     # in 1st iteration carry will be 0, but in next iterations previous iter generated carry will be added
            carry = val // 10         # if val = 15 then 15//10 = 1 ie. (1.5)
            val = val % 10            # 15 % 10 = 5
            cur.next = ListNode(val)  # dummy/cur --> val

            # Update pointers
            cur = cur.next            # dummy --> val/cur
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1 = list_to_LL([1,2,3])
l2 = list_to_LL([4,5,6])

solution = Solution2()
print(solution.addTwoNumbers(l1, l2))
