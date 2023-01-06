## [Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/)

* **C++**
```cpp
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(),costs.end());
        
        for(int i = 0; i < costs.size(); i++)
            if((coins -= costs[i]) < 0)
                return i;
        return costs.size();
    }
};
```

* **PYTHON**
```py
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        for i in range(len(costs)):
            coins -= costs[i]
            if(coins < 0):
                return i
            
        return len(costs) 
```
