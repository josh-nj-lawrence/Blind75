# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = pnt = ListNode(0)
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        
        for x in sorted(nodes):
            pnt.next = ListNode(x)
            pnt = pnt.next

        return head.next
    
# Results: 88.1% time (97ms) 24.58% space (18.4MB)