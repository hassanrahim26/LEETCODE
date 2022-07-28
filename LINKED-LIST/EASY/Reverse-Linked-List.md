## [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

* **C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *curr = NULL;
        while(head){
            ListNode *temp = head->next;
            head->next = curr;
            curr = head;
            head = temp;
        }
        return curr;
    }
};
```

* **Python**
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        while(head):
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr
```
