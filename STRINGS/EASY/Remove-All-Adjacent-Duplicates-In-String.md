## [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

* **C++**
 
  * 1
  ```cpp
  class Solution {
  public:
      string removeDuplicates(string s) {
          string ans = "";
          for(auto c: s){
              if(ans.size() and ans.back() == c)  ans.pop_back();
              else ans.push_back(c);
          }
          return ans;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      string removeDuplicates(string s) {
          int i = 0, n = s.length();
          for(int j = 0; j < n; j++, i++){
              s[i] = s[j];
              if(i > 0 and s[i-1] == s[i])    
                  i -= 2;
          }
          return s.substr(0, i);
      }
  };
  ```
<hr>

* **PYTHON**
```py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)
        
```
