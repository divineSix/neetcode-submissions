# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2 # pointers to two nodes. 

        # Both valid lists
        ptr = None
        while p1 and p2:
            print(f"Comparing: P1 {p1.val}, P2 {p2.val}")
            print("Ptr: ", ptr.val if ptr else None)
            if p1.val < p2.val: # 
                if ptr: # ptr exists.  
                    ptr.next = p1
                    ptr = ptr.next
                else:
                    ptr = p1
                # ptr = p1
                p1 = p1.next
            else:
                if ptr: 
                    ptr.next = p2
                    ptr = ptr.next
                else:
                    ptr = p2
                p2 = p2.next

        if p1 is None: # p2 elements are still pending. 
            if ptr:
                ptr.next = p2
            else: 
                ptr = p2
        
        if p2 is None:
            if ptr: 
                ptr.next = p1
            else:
                ptr = p1

        if list1 and list2:
            new_head = list1 if list1.val < list2.val else list2
        elif list1: 
            new_head = list1
        else:
            new_head = list2
        return new_head
