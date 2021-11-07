# PROBLEM LINK:- https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        self.ans = self.reverseList(head.next)
        self.tail = head.next
        self.tail.next = head
        head.next = None
        return self.ans
