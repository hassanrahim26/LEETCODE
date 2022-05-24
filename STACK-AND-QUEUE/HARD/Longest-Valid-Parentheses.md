## [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

* **C++**
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int ans = 0;
        
        for(int i = 0; i < s.size(); i++){
            int t = st.top();
            if(t != -1 and s[i] == ')' and s[t] == '(')
            {
                st.pop();
                ans = max(ans, i - st.top());
            }
            else
                st.push(i);
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif len(st) == 1:
                st[0] = i
            else:
                st.pop()
                ans = max(ans, i - st[-1])
        
        return ans
```
