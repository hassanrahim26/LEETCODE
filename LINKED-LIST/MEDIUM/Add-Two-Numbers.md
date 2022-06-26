## [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3 = new ListNode(), *temp = l3;
        int carry = 0;
        
        while(l1 || l2 || carry)
        {   
            if(l1 != NULL)
            {
                carry += l1->val;
                l1 = l1->next;
            }
            
            if(l2 != NULL)
            {
                carry += l2->val;
                l2 = l2->next;
            }
            
            temp->next = new ListNode(carry%10);
            carry /= 10;
            temp = temp->next;
        }
        
        return l3->next;
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = temp = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            temp.next = ListNode(carry%10)
            carry //= 10
            temp = temp.next
        
        return l3.next
```
