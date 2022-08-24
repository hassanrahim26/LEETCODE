## [Power of Three](https://leetcode.com/problems/power-of-three/)

* **C++**
  * 1
    ```cpp
       class Solution {
       public:
          bool isPowerOfThree(int n) {
             if(n == 0)    
                 return false;
             while(n % 3 == 0)
                 n /= 3;
             return n == 1;
          }
       };
    ```
    
  * 2
    ```cpp
    class Solution {
    public:
        bool isPowerOfThree(int n) {
           return n > 0 && 1162261467 % n == 0;
        }
    };
    ```
    
  * 3
    ```cpp
    class Solution {
    public:
        bool isPowerOfThree(int n) {
            if(n <= 1)
                return n == 1;
            return n % 3 == 0 and isPowerOfThree(n/3);
        }
    };
    ```
<hr>

* **Python**
  * 1
    ```py
    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            if n == 0:
                return False
            while(n%3 == 0):
                n /= 3
            return n == 1    
    ```
  
  * 2
    ```py
    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            return n > 0 && 1162261467 % n == 0
    ```
  
  * 3
    ```py
    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            if(n <= 1):
                return n == 1
            return n % 3 == 0 and self.isPowerOfThree(n//3)
    ```
