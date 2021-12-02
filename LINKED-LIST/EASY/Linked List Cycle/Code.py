# PROBLEM LINK:- https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head;
        
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False
