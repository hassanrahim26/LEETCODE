## [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      int climbStairs(int n) {
          int a[n+1];
          a[0] = 1, a[1] = 1;
          for(int i = 2; i <= n; i++){
              a[i] = a[i-2] + a[i-1];
          }
          return a[n];
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int climbStairs(int n) {
          if(n <= 2) return n;
          int a = 1, b = 2, ans;
          for(int i = 3; i <= n; i++){
              ans = a + b;
              a = b;
              b = ans;
          }
          return ans;
      }
  };
  ```

<hr>

* **Python**

  * 1
  ```py
  class Solution:
      def climbStairs(self, n: int) -> int:
          arr = [1, 1]
          for i in range(2, n+1):
              arr.append(arr[i-2] + arr[i-1])
          return arr[n] 
  ```
  
  * 2
  ```py
  class Solution:
      def climbStairs(self, n: int) -> int:
          if(n <= 2): return n
          a, b, ans = 1, 2, 0
          for i in range(3, n+1):
              ans = a + b
              a = b
              b = ans
          return ans
  ```
