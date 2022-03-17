## [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

* **C++**
```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head)
            return head;
        ListNode* temp = head;
        
        while(temp && temp->next)
        {
            if(temp->val == temp->next->val)
                temp->next = temp->next->next;
            else
                temp = temp->next;
        }
        
        return head;
    }
};
```

* **Python**
```py
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head;
        
        temp = head
        
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
```
