## [Interleaving String](https://leetcode.com/problems/interleaving-string/)

* **C++**
```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        vector<bool> dp1(s2.size()+1, 0), dp2(s2.size()+1, 0);
        if(s3.size() != s1.size() + s2.size())
            return false;
        
        for(int i = s1.size(); i >= 0; i--)
        {
            for(int j = s2.size(); j >= 0; j--)
            {
                if(i == s1.size() and j == s2.size())
                    dp1[j] = 1;
                else if(s3[i+j] == s2[j] and s3[i+j] == s1[i])
                    dp1[j] = dp1[j+1] || dp2[j];
                else if(s1[i] == s3[i+j])
                    dp1[j] = dp2[j];
                else if(s3[i+j] == s2[j])
                    dp1[j] = dp1[j+1];
                else
                    dp1[j] = 0;
            }
            dp2 = dp1;
        }
        return dp1[0];
    }
};
```

* **Python**
```py
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1), len(s2)
        dp1, dp2 = [False]*(n+1), [False]*(n+1)
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                dp1[j] = False
                
                if i == m and j == n:
                    dp1[n] = True
                if i < m and s1[i] == s3[i+j]:
                    dp1[j] |= dp2[j]
                if j < n and s2[j] == s3[i+j]:
                    dp1[j] |= dp1[j+1]
            dp1, dp2 = dp2, dp1
            
        return dp2[0]
```
