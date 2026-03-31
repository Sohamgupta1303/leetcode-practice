# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None;
        
        head = ListNode();
        current = head; 
        prev = None;
        
        while (list1 is not None and list2 is not None):
            if (list1.val > list2.val):
                current.val = list2.val;
                if (prev is not None):
                    prev.next = current;
                prev = current;
                list2 = list2.next;
                current = ListNode();
            else:
                current.val = list1.val;
                if (prev is not None):
                    prev.next = current;
                prev = current;
                list1 = list1.next;
                current = ListNode();
        
        iterator = ListNode();
        if list1 is None and list2 is not None:
            iterator = list2;
        elif list2 is None and list1 is not None:
            iterator = list1;
        elif list1 is None and list2 is None:
            return head;

        while (iterator is not None):
            current.val = iterator.val;
            if prev is not None:
                prev.next = current;
            prev = current;
            current = ListNode();
            iterator = iterator.next;
        
        return head;
        


                
            


        

        