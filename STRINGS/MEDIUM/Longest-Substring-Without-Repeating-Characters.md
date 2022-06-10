## [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

* **C++**
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> st;
        int i = 0, j = 0, n = s.size(), ans = 0;
        
        while(j < n){
            if(st.find(s[j]) == st.end())
            {
                st.insert(s[j++]);
                ans = max(ans, j-i);
            }
            else
            {
                st.erase(s[i++]);
            }
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        j, ans = 0, 0
        
        for i in range(len(s)):
            if s[i] not in st:
                ans = max(ans, i - j + 1)
            else:
                if st[s[i]] < j:
                    ans = max(ans, i - j + 1)
                else:
                    j = st[s[i]] + 1
            st[s[i]] = i
        
        return ans
```
