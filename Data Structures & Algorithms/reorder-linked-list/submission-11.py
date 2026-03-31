# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math;

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # getting number of elements
        current = head;
        len = 0;
        while (current is not None):
            len += 1;
            current = current.next;
        # reversing second half 
        # connecting nodes in order
        left = head;
        right = head;
        count = 0;

        while count < math.ceil(len/2):
            count += 1;
            right = right.next;

        # we are now at the first node to be reversed
        prev = None;
        while (right):
            next_node = right.next;
            right.next = prev;
            prev = right
            right = next_node;
        right = prev
            
        #prev should be the last real node
        #now we can start reordering
        left_ptr = head
        while left_ptr and right:
            left_next, right_next = left_ptr.next, right.next
            left_ptr.next = right
            right.next = left_next
            left_ptr, right = left_next, right_next

        if left_ptr:
            left_ptr.next = None



        




