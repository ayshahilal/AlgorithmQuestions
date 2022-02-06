# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = 0
        n2 = 0 
        x = 1 
        current = l1
        while(current.next):
            n1 += current.val * x
            x = x*10
            current = current.next
        n1 += current.val * x
     
        x = 1     
        current = l2
        while(current.next):
            n2 += current.val * x
            x = x*10
            current = current.next
        n2 += current.val * x
        num = n1 + n2

        
                  
        x = [int(a) for a in str(num)]
 
        result = ListNode(x[len(x)-1])
        current = result
        for i in range(len(x)-2, -1, -1):
            new = ListNode(x[i])
            current.next = new
            current = current.next

            
        return result
