## [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

* **C++**
```cpp
class Solution {
public:
    bool isPossible(vector<int>& v) {
        unordered_map<int, int> mp1, mp2;
        for(auto x: v)
            mp1[x]++;
        
        for(auto x: v){
            if(mp1[x] == 0)  continue;
            mp1[x]--;
            
            if(mp2[x-1] > 0){
                mp2[x-1]--;
                mp2[x]++;
            }
            else if(mp1[x+1] > 0 and mp1[x+2] > 0){
                mp1[x+1]--;
                mp1[x+2]--;
                mp2[x+2]++;
            }
            else
                return false;
        }
        return true;
    }
};
```

* **PYTHON**
```py
class Solution:
    def isPossible(self, v: List[int]) -> bool:
        mp1 = collections.Counter(v)
        mp2 = collections.Counter()
        
        for x in v:
            if not mp1[x]:  continue
            mp1[x] -= 1
            
            if mp2[x-1] > 0:
                mp2[x-1] -= 1
                mp2[x] += 1
            elif mp1[x+1] and mp1[x+2]:
                mp1[x+1] -= 1
                mp1[x+2] -= 1
                mp2[x+2] += 1
            else:
                return False
        return True
```
