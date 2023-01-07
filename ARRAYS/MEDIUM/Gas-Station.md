## [Gas Station](https://leetcode.com/problems/gas-station/)

* **C++**
```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int l = gas.size()-1, r = 0, s = gas[l] - cost[l];
        
        while(l > r){
            if(s >= 0){
                s += gas[r] - cost[r];
                r++;
            }
            else{
                l--;
                s += gas[l] - cost[l];
            }
        }
        return s >= 0 ? l : -1;
    }
};
```

* **PYTHON**
```py
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l, r = len(gas)-1, 0
        s = gas[l] - cost[l]
        
        while(l > r):
            if(s >= 0):
                s += gas[r] - cost[r]
                r += 1
            else:
                l -= 1
                s += gas[l] - cost[l]
                
        return l if s >= 0 else -1
```
