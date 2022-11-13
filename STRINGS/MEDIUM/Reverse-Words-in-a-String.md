## [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

* **C++**
```cpp
class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());
        int l = 0, r = 0, i = 0, n = s.size();
        while(i < n){
            while(i < n and s[i] != ' ')
                s[r++] = s[i++];
            if(l < r){
                reverse(s.begin()+l, s.begin()+r);
                if(r == n) break;
                s[r++] = ' ';
                l = r;
            }
            ++i;
        }
        if(r > 0 and s[r-1] == ' ') --r;
        s.resize(r);
        return s;
    }
};
```

* **PYTHON**
```py
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
```
