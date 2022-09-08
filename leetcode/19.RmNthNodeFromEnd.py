# https://leetcode.com/problems/remove-nth-node-from-end-of-list/ 
from lcutils import * 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers, one is n steps further from another 
        pred_ptr = succ_ptr = head
        # move the predecessor by n steps 
        # (the linked list may contain less than n elements, in this case
        # we should not remove any element)
        for _ in range(n): 
            try:
                pred_ptr = pred_ptr.next 
            except:
                return head
            
        # if the pred_ptr is None, it means n=length_of_list
        # then we remove the head
        if pred_ptr is None:
            return head.next
        
        # if n < length_of_list 
        # move pred_ptr to the end of the list
        # and succ_ptr is n steps behind it (so we remove the next of succ_ptr)
        while pred_ptr.next is not None:
            pred_ptr = pred_ptr.next 
            succ_ptr = succ_ptr.next 
        
        succ_ptr.next = succ_ptr.next.next 
        
        return head 
    
    

head = make_linked_list([1,2,3,4,5])
ans = Solution().removeNthFromEnd(head, 1)
print(ans)
    
    