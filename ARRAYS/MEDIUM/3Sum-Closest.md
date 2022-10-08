## [3Sum Closest](https://leetcode.com/problems/3sum-closest/)

* **C++**
```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), j, k, res = nums[0] + nums[1] + nums[2];
        
        for(int i = 0; i < n-2; i++){
            int l = i+1, r = n-1;
            while(l < r){
                int s = nums[i] + nums[l] + nums[r];
                if(abs(res-target) > abs(s-target))
                    res = s;
                if(s == target)
                    break;
                if(s > target)
                    r--;
                else
                    l++;
            }
        }
        return res;
    }
};
```

* **PYTHON**
```py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            l, r = i+1, n-1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if(abs(res-target) > abs(s-target)):
                    res = s
                if(s == target):
                    break
                if(s > target):
                    r -= 1
                else:
                    l += 1
        return res
```
