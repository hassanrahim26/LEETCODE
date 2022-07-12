## [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

* **C++**
```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n1 = p.size(), n2 = s.size();
        vector<int> v1(26, 0), v2(26, 0), ans;
        for(char c: p)
            v1[c - 'a']++;
        
        for(int i = 0; i < n2; i++){
            v2[s[i] - 'a']++;
            
            if(i >= n1)
                v2[s[i - n1] - 'a']--;
            if(v1 == v2)
                ans.push_back(i - n1 + 1);
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(p), len(s)
        v1 = [0]*26
        v2 = [0]*26
        ans = []
        
        for c in p:
            v1[ord(c) - ord('a')] += 1
        
        for i in range(n2):
            v2[ord(s[i]) - ord('a')] += 1
            
            if i >= n1:
                v2[ord(s[i-n1]) - ord('a')] -= 1
            if v1 == v2:
                ans.append(i-n1+1)
                
        return ans
```
