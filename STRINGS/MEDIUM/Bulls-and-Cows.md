## [Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/)

* **C++**
```cpp
class Solution {
public:
    string getHint(string secret, string guess) {
        int a = 0, b = 0;
        vector<int> v1(10, 0), v2(10, 0);
        if(secret.size() != guess.size() || secret.empty())
            return "0A0B";
        
        for(int i = 0; i < secret.size(); i++){
            char c1 = secret[i], c2 = guess[i];
            if(c1 == c2)
                a++;
            else
            {
                v1[c1 - '0']++;
                v2[c2 - '0']++;
            }
        }
        
        for(int i = 0; i < v1.size(); i++)
            b += min(v1[i], v2[i]);
        
        return to_string(a) + 'A' + to_string(b) + 'B';
    }
};
```

* **Python**
```py
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        v1 = [0]*10
        v2 = [0]*10
        
        if len(secret) != len(guess) or len(secret) == 0:
            return "0A0B"
        
        for i in range(len(secret)):
            c1, c2 = secret[i], guess[i]
            if c1 == c2:
                a += 1
            else:
                v1[ord(c1) - ord('0')] += 1
                v2[ord(c2) - ord('0')] += 1
        
        for i in range(len(v1)):
            b += min(v1[i], v2[i])
        
        return str(a) + 'A' + str(b) + 'B'
```
