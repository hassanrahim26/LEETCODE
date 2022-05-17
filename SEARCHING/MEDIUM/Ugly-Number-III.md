## [Ugly Number III](https://leetcode.com/problems/ugly-number-iii/)

* **C++**
```cpp
class Solution {
public:
    long long lcm(long long a, long long b) {
        return a*b / __gcd(a, b);
    }
    
    int nthUglyNumber(int n, int a, int b, int c) {
        long long low = 1, high = 2000000000, mid, ans;
        
        while(low <= high){
            mid = low + (high - low)/2;
            long long count = 0;
            count += mid/a;
            count += mid/b;
            count += mid/c;
            count -= mid/lcm(a,b);
            count -= mid/lcm(b,c);
            count -= mid/lcm(c,a);
            count += mid/lcm(a, lcm(b, c));
            
            if(count >= n){
                ans = mid;
                high = mid - 1;
            }
            else
                low = mid + 1;
        }
        return ans;
    }
};
```
