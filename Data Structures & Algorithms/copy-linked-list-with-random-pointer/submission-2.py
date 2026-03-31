"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_copy = {}
        node = head
        copy = Node(0)
        toret = copy
        if (head is None):
            return head
        while (node is not None):
            if (node in node_copy):
                copy = node_copy[node]
            else:
                copy.val = node.val
                node_copy[node] = copy
            
            # random part
            if (node.random and node.random in node_copy):
                copy.random = node_copy[node.random]
            elif(not node.random):
                copy.random = None
            else:
                copy_random = Node(node.random.val)
                copy.random = copy_random
                node_copy[node.random] = copy_random
            
            #next part
            if (node.next and node.next in node_copy):
                copy.next = node_copy[node.next]
            elif (not node.next):
                copy.next = None
            else:
                copy_next = Node(node.next.val)
                copy.next = copy_next
                node_copy[node.next] = copy_next
            
            node = node.next
            copy = copy.next
        
        return toret



            


        