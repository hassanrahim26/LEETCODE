## [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

* **C++**
  
  * 1
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
      ListNode* deleteMiddle(ListNode* head) {
          if(head->next == NULL)
              return NULL;
          ListNode *slow = head, *fast = head->next->next;
          while(fast != NULL and fast->next != NULL){
              fast = fast->next->next;
              slow = slow->next;
          }
          slow->next = slow->next->next;
          return head;
      }
  };
  ```
  
  * 2
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
      ListNode* deleteMiddle(ListNode* head) {
          ListNode *slow = head, *fast = head, *prev = NULL;
          while(fast != NULL and fast->next != NULL){
              prev = slow;
              slow = slow->next;
              fast = fast->next->next;
          }
          if(prev == NULL)
              return NULL;
          prev->next = slow->next;
          return head;
      }
  };
  ```
  
  
* **PYTHON**

  * 1
  ```py
  # Definition for singly-linked list.
  # class ListNode: 
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if(head.next == None):
              return None
          slow, fast = head, head.next.next
          while(fast != None and fast.next != None):
              fast = fast.next.next
              slow = slow.next
          slow.next = slow.next.next
          return head
  ```
  
  * 2
  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
          slow, fast, prev = head, head, None
          while(fast != None and fast.next != None):
              prev = slow
              slow = slow.next
              fast = fast.next.next

          if(prev == None):
              return None
          prev.next = slow.next
          return head
  ```
