## [Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
          string s1 = "", s2 = "";
          for(int i = 0; i < word1.size(); i++)    
          {
            s1 += word1[i];
          }
        
          for(int j = 0; j < word2.size(); j++)
          {
            s2 += word2[j];
          }
        
          if(s1 == s2)
              return true;
          return false;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
          string s1, s2;
          for(auto a : word1) s1 += a;
          for(auto b : word2) s2 += b;
          return s1 == s2;
      }
  };
  ```
  
* **PYTHON**
```py
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
```
