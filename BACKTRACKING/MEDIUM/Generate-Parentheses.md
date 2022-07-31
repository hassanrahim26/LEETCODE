## [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

* **C++**
```cpp
class Solution {
public:
    void solve(vector<string>& ans, string s, int n, int m){
        if(n == 0 and m == 0){
            ans.push_back(s);
            return;
        }
        if(n > 0) {solve(ans, s + "(", n-1, m+1);}
        if(m > 0) {solve(ans, s + ")", n, m-1);}
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        solve(ans, "", n, 0);
        return ans;
    }  
};
```

* **Python**
```py
class Solution:
    def solve(self, ans, s, n, m):
        if n == 0 and m == 0:
            ans.append(s)
            return
        
        if n > 0: self.solve(ans, s + "(", n-1, m+1)
        if m > 0: self.solve(ans, s + ")", n, m-1)
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.solve(ans, "", n, 0)
        return ans
```
