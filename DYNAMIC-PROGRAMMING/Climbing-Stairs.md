## [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

* **C++**
```cpp
class Solution {
public:
    int climbStairs(int n) {
        int a[n+1];
        a[0] = 1, a[1] = 1;
        for(int i = 2; i <= n; i++)
        {
            a[i] = a[i-2] + a[i-1];
        }
        
        return a[n];
    }
};
```
* **Python**
```py
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]
        for i in range(2, n+1):
            arr.append(arr[i-2] + arr[i-1])
        return arr[n]
        
```
