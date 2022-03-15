## [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

* **C++**
1. Recursive
```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(!head)
            return NULL;
        head->next = removeElements(head->next, val);
        return (head->val == val) ? head->next : head;
    }
};
```

2. Iterative
```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        while(head && head->val == val)
            head = head->next;
        
        ListNode *temp = head;
        while(temp)
        {
            if(temp->next && temp->next->val == val)
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
```
