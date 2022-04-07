## [Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

* **C++**
```cpp
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int ans = 0, n = arr.size();
        for(int i = 0; i < n; i++)
        {
            ans += ((i + 1) * (n - i) + 1)/2 * arr[i];
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, freq, n = 0, 0, len(arr)
        for i in range(n):
            freq = freq - (i+1)//2 + (n-i+1)//2
            ans += freq * arr[i]
        return ans
```
