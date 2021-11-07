/*
PROBLEM LINK:- https://leetcode.com/problems/reverse-linked-list/
*/

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head -> next == NULL)    
            return head;
        ListNode *ans = reverseList(head -> next);
        ListNode *tail = head -> next;
        tail -> next = head;
        head -> next = NULL;
        return ans;
    }
};
