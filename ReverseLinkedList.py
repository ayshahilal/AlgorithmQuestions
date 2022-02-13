

#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
        

def reverseLinkedList(head):
    # Original: a -> b -> c -> d -> none 
    # Reversed: d -> c -> b -> a -> none 
    
    current = head
    previous = None
    
    while(current):   
        next_node = current.next    
        current.next = previous   
        previous = current
        
        if not next_node:
            break
        
        current = next_node

    return current
    

if __name__ == '__main__':
    
    # Creating example linked list 
    
    link = ListNode("a")
    link.next =  ListNode("b")
    link.next.next = ListNode("c")
    link.next.next.next = ListNode("d")
  
 
    reversedList = reverseLinkedList(link)
    
    # Print result 
    print("Reversed Linked List is: ")
    while(reversedList.next): 
        print(reversedList.val)
        reversedList = reversedList.next 
    print(reversedList.val)
    
