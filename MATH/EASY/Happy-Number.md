## [Happy Number](https://leetcode.com/problems/happy-number/)

* **C++**
```cpp
class Solution {
public:
    bool isHappy(int n) {
        unordered_map<int, int> mp;
        while(n != 1)
        {
            if(mp[n] == 0)
                mp[n]++;
            else
                return false;
            
            int sum = 0;
            while(n != 0)
            {
                sum += pow(n%10, 2);
                n /= 10;
            }
            n = sum;
        }
        
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 4:
            n = sum(int(d)**2 for d in str(n))
        return n == 1
```
