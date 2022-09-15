## [Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/)

* **C++**
```cpp
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& c) {
        int n = c.size();
        if(n % 2 == 1) return {};
        
        sort(c.begin(), c.end());
        vector<int> ans;
        
        unordered_map<int, int> mp;
        for(auto x: c)
            mp[x]++;
        
        for(int i = 0; i < n; i++){
            if(mp[c[i]] == 0) continue;
            if(mp[c[i] * 2] == 0) return {};
            ans.push_back(c[i]);
            mp[c[i]]--;
            mp[c[i] * 2]--;
        }
        
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def findOriginalArray(self, c: List[int]) -> List[int]:
        mp = collections.Counter(c)
        c.sort()
        ans = []
        for x in c:
            if mp[x] > 0:
                mp[x] -= 1
                if mp[x*2] > 0:
                    mp[x*2] -= 1
                    ans.append(x)
                else:
                    return []
        return ans
```
