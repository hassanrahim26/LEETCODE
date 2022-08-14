## [Construct Smallest Number From DI String](https://leetcode.com/problems/construct-smallest-number-from-di-string/)

* **C++**
```cpp
class Solution {
public:
    string smallestNumber(string p) {
        string ans;
        stack<int> s;
        for (int i = 0; i <= p.length(); i++){
            s.push(i + 1);
            if (i == p.length() || p[i] == 'I'){
                while (!s.empty()){
                    ans += to_string(s.top());
                    s.pop();
                }
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def smallestNumber(self, p: str) -> str:
        ans = ""
        s = []
        n = 1
        for i in range(len(p)):
            s.append(n)
            n += 1
            if(p[i] != 'D'):
                while(s):
                    k = s.pop()
                    ans += str(k)
        s.append(n)
        while(s):
            k = s.pop()
            ans += str(k)
        return ans
```
