## [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

* 1
    ```cpp
    /**
    * Definition for singly-linked list.
    * struct ListNode {
    *     int val;
    *     ListNode *next;
    *     ListNode() : val(0), next(nullptr) {}
    *     ListNode(int x) : val(x), next(nullptr) {}
    *      ListNode(int x, ListNode *next) : val(x), next(next) {}
    * };
    */
    class Solution {
    public:
        bool isPalindrome(ListNode* head) {
            ListNode *fast = head, *slow = head;
        
            while(fast && fast -> next)
            {
                slow = slow -> next;
                fast = fast -> next -> next;
            }
        
            ListNode *mid = slow, *prev = NULL, *next = NULL;
        
            while(mid)
            {
                next = mid -> next;
                mid -> next = prev;
                prev = mid;
                mid = next;
            }
        
            ListNode *tail = prev;
        
            while(head && tail && tail != head)
            {
                if(tail -> val  != head -> val)
                    return false;
                head = head -> next;
                tail = tail -> next;
            }
        
            return true;
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
            ListNode *temp;
            bool isPalindrome(ListNode* head) {
                temp = head;
                return solve(head);
            }
    
            bool solve(ListNode* p){
                if(p == NULL)   return true;
                bool check = solve(p->next) & (temp->val == p->val);
                temp = temp->next;
                return check;
            }
        };
    ```
