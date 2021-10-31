# PROBLEM LINK:- https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val >= l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            l2 = l1
        return l2
        
