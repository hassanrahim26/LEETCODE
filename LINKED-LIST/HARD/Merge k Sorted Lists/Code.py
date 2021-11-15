# PROBLEM LINK:- https://leetcode.com/problems/merge-k-sorted-lists/

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
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        x = len(lists)
        
        while(x > 1):
            for i in range(0, x//2):
                lists[i] = self.mergeTwoLists(lists[i], lists[x - 1 - i])
            x = (x + 1)//2
        return lists[0]
