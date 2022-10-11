## [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)

* **C++**
```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int c1 = INT_MAX, c2 = INT_MAX;
        for(int x: nums){
            if(x <= c1)
                c1 = x;
            else if(x <= c2)
                c2 = x;
            else
                return true;
        }
        return false;
    }
};
```

* **PYTHON**
```py
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        c1 = c2 = float('inf')
        for x in nums:
            if(x <= c1):
                c1 = x
            elif(x <= c2):
                c2 = x;
            else:
                return True;
        return False;
```
