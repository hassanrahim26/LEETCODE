# PROBLEM LINK:- https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
            
        return True
                
