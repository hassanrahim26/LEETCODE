## [Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)

* **C++**
```cpp
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode *node1 = head;
        ListNode *node2 = head;
        ListNode *curr = head;
        
        int c = 1;
        
        while(curr != NULL)
        {
            if(c < k)
                node1 = node1->next;
            if(c > k)
                node2 = node2->next;
            
            curr = curr->next;
            c++;
        }
        
        int temp = node1->val;
        node1->val = node2->val;
        node2->val = temp;
        
        return head;
    }
};
```

* **Python**
```py
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1, node2, curr = head, head, head
        c = 1
        
        while curr != None:
            if c < k:
                node1 = node1.next
            if c > k:
                node2 = node2.next
            curr = curr.next
            c += 1
            
        temp = node1.val
        node1.val = node2.val
        node2.val = temp
        
        return head
```
