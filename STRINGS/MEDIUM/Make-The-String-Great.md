## [Make The String Great](https://leetcode.com/problems/make-the-string-great/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      string makeGood(string s) {
          string ans;
          for(int i = 0 ; i < s.size() ; i++){
              ans.push_back(s[i]);
              while(ans.size() && (ans.back()==s[i+1]+32 || ans.back()==s[i+1]-32)){
                  ans.pop_back();
                  i++;
              }
          }
          return ans;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      string makeGood(string s) {
          int j = 0;
          for(int i = 0; i < s.size(); i++){
               if(j > 0 and abs(s[i] - s[j-1]) == 32)
                  j--;
              else{
                  s[j] = s[i];
                  j++;
              }
          } 
          return s.substr(0, j);
      }
  };
  ```
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def makeGood(self, s: str) -> str:
          i = 0
          while(i < len(s)-1):
              if((ord(s[i]) - ord(s[i+1]) == 32) or ord(s[i]) - ord(s[i+1]) == -32):
                  s = s[:i] + s[i+2:]
                  if i > 0:
                      i -= 1
              else:
                  i += 1
          return s                
  ```
