# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        ret = ListNode()
        trav = ret

        while l1 or l2 or carry:
            trav.next = ListNode()
            trav = trav.next
            val = 0
            if l1: val += l1.val
            if l2: val += l2.val
            val += carry

            trav.val = val % 10
            carry = val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            trav.val = carry
        
        return ret.next
        
        

        
            


        