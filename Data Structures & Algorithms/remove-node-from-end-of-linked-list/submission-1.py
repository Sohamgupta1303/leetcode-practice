# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 0;

        while (current):
            size += 1;
            current = current.next;
        
        current = head;
        prev = None;
        count = 0;
        while (current):
            count += 1;
            if (count == size - (n - 1)):
                if (current == head):
                    head = current.next;
                    current.next = None;
                else:
                    prev.next = current.next;
        
            prev = current;
            current = current.next;

        return head;
            
                 


        