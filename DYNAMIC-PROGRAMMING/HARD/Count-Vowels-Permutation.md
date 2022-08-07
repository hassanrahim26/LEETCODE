## [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/)

* **C++**
```cpp
class Solution {
public:
    int countVowelPermutation(int n) {
        long a = 1, e = 1, i = 1, o = 1, u = 1, mod = pow(10, 9)+7;
        long a1, e1, i1, o1, u1; 
    
        for (int j = 2; j <= n; j++) {
            a1 = (e + i + u) % mod;
            e1 = (a + i) % mod;
            i1 = (e + o) % mod;
            o1 = i;
            u1 = (o + i) % mod;
            
            a = a1, e = e1, i = i1, o = o1, u = u1;
        }
        return (a + e + i + o + u) % mod;
    }
};
```

* **PYTHON**
```py
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n-1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)
```
