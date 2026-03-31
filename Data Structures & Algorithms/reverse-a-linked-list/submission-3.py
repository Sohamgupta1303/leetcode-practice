# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None;
        current = head;
        prev = None;
        while (current.next != None):
            curr_next = current.next;
            current.next = prev;
            prev = current;
            current = curr_next;
        
        current.next = prev;

        
        return current;
        