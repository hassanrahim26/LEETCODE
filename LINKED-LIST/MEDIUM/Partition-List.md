## [Partition List](https://leetcode.com/problems/partition-list/)

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
    ListNode* partition(ListNode* head, int x) {
        ListNode *node1 = new ListNode(0), *node2 = new ListNode(0);
        ListNode *p1 = node1, *p2 = node2;
        
        while(head != NULL)
        {
            if(head->val < x){
                p1->next = head;
                p1 = p1->next;
            }
            else{
                p2->next = head;
                p2 = p2->next;
            }
            head = head->next;
        }
        p1->next = node2->next;
        p2->next = NULL;
        return node1->next;
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node1 = p1 = ListNode(0)
        node2 = p2 = ListNode(0)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
    
        p1.next = node2.next
        p2.next = None
        return node1.next
```
