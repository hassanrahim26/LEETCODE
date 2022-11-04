## [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

* **C++**
```cpp
class Solution {
public:
    bool isVowel(char c){
        c = tolower(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    string reverseVowels(string s) {
        int n = s.size(), l = 0, r = n-1;
        while(l < r){
            while(l < r and !isVowel(s[l]))
                l++;
            while(r > l and !isVowel(s[r]))
                r--;
            swap(s[l], s[r]);
            l += 1;
            r -= 1;
        }
        return s;
    }
};
```

* **PYTHON**
```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        l, r = 0, n-1
        s = list(s)
        vowels = list("aeiouAEIOU")
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while r > l and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
```
