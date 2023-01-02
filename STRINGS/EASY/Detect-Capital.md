## [Detect Capital](https://leetcode.com/problems/detect-capital/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      bool detectCapitalUse(string word) {
          int n = word.size(), c = 0;
          for(auto x: word){
              if(x >= 'A' and x <= 'Z')
                  c++;
          }
          if(c == n or c == 0 or (word[0] >= 'A' and word[0] <= 'Z' and c == 1))
              return true;
          return false;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      bool detectCapitalUse(string word) {
          for(int i = 1; i < word.size(); i++){
              if((isupper(word[1]) != isupper(word[i])) || (islower(word[0]) && isupper(word[i])))
                  return false;
          }
          return true;
      }
  };
  ```
  
<hr>

* **PYTHON**
  
  * 1
  ```py
  class Solution:
      def detectCapitalUse(self, word: str) -> bool:
          n, c = len(word), 0
          for x in word:
              if(x >= 'A' and x <= 'Z'):
                  c += 1
        
          if(c == n or c == 0 or (word[0] >= 'A' and word[0] <= 'Z' and c == 1)):
              return True
          return False
  ```
  
  * 2
  ```py
  class Solution:
      def detectCapitalUse(self, word: str) -> bool:
          for i in range(1, len(word)):
              if((word[1].isupper() != word[i].isupper()) or (word[0].islower() and word[i].isupper())):
                  return False
          return True
  ```
