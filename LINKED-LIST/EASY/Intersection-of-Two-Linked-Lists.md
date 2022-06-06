## [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

* **C++**
```cpp
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *temp1 = headA, *temp2 = headB;
        while(temp1 != temp2){
            temp1 = !temp1 ? headB : temp1->next;
            temp2 = !temp2 ? headA : temp2->next;
        }
        return temp1;
    }
};
```

* **Python**
```py
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1, temp2 = headA, headB
        while(temp1 != temp2):
            temp1 = headB if not temp1 else temp1.next
            temp2 = headA if not temp2 else temp2.next
        return temp1
```
