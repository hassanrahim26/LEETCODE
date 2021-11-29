/*
PROBLEM LINK:- https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
*/

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int ans = 0;
        while(head)
        {
            ans = (ans << 1) + head -> val;
            head = head -> next;
        }
        
        return ans;
    }
};
