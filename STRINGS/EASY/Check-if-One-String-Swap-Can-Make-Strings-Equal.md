## [Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)

* **C++**
```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> idx;
        
        for(int i = 0; i < s1.size(); i++)
        {
            if(s1[i] != s2[i])
                idx.push_back(i);
            
            if(idx.size() >= 2)
                break;
        }
        
        if(idx.size() == 1)
            return false;
        
        else if(idx.size() == 0)
            return true;
        
        else
        {
            swap(s2[idx[0]], s2[idx[1]]);
            return s1 == s2;
        }
    }
};
```

* **Python**
```py
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1
            if c > 2:
                return False
        return True 
```
