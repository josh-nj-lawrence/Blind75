# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val

def printList(l1):
    while l1 != None:
        print(l1.val, "->", end=" ")
        l1=l1.next
    print("None")

def mergeTwoLists(list1, list2):
    # Cheap solution
    l3 = ListNode()
    position = l3
    while list1!=None and list2!=None:
        if list1.val<list2.val:
            position.next=list1
            list1 = list1.next
        else:
            position.next=list2
            list2 = list2.next    
        position = position.next
    if list1==None:
        position.next = list2
    else:
        position.next = list1
    return l3.next
        
list1 = ListNode(1)
list1.next = ListNode(2)

list2 = ListNode(1)
list2.next = ListNode(5)
printList(mergeTwoLists(list1,list2))