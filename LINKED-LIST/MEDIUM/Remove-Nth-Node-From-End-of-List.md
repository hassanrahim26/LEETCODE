## [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

* **C++**
```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fast = head, *slow = head;    
        for(int i = 0; i < n; i++)
            fast = fast->next;
        if(!fast)
            return head->next;
        while(fast->next)
        {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        
        return head;
    }
};
```
* **PYTHON**
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast: return head.next
        
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        
        return head
```
