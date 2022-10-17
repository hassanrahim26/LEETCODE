## [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      bool checkIfPangram(string str) {
          int n = str.size();
          vector v(26,0);
        
          for(int i = 0; i < n; i++)
          {
              v[str[i]-'a']++;
          }
        
          for(int i = 0; i < v.size(); i++)
          {
              if(v[i] == 0)
                  return false;
          }
          return true;
      }
  };
  ```
 
  * 2
  ```cpp
  class Solution {
  public:
      bool checkIfPangram(string s) {
          return set<char>(s.begin(), s.end()).size() == 26;;
      }
  };
  ```
  
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(s)) == 26
  ```
