## [Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

* **C++**
```cpp
class Solution {
public:
    int mod = 1000000007;
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int ans = 0, n = nums.size(), i = 0, j = n - 1;
        
        vector<int> v(n+1, 1);
        
        for(int i = 1; i <= n; i++){
            v[i] = (2 * v[i - 1])%mod;
        }
        
        while(i <= j){
            if(nums[i] + nums[j] <= target){
                ans = (ans + v[j - i]) % mod;
                i++;
            }
            
            else
                j--;
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        
        mod = 10**9 + 7
        i, j = 0, n-1
        
        for i in range(n):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            
            if i <= j and nums[i] + nums[j] <= target:
                ans += pow(2, (j - i), mod)
                ans %= mod
        
        return ans
```
