## [Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/)

* **C++**
```cpp
class Solution {
public:
    string breakPalindrome(string p) {
        int n = p.size();
        for(int i = 0; i < p.size()/2; i++){
            if(p[i] != 'a'){
                p[i] = 'a';
                return p;
            }
        }
        p[n-1] = 'b';
        return n < 2 ? "" :  p;
    }
};
```

* **PYTHON**
```py
class Solution:
    def breakPalindrome(self, p: str) -> str:
        n = len(p)
        for i in range(n//2):
            if p[i] != "a":
                return p[:i] + "a" + p[i+1:]
        return p[:-1] + "b" if n > 1 else ""
```
