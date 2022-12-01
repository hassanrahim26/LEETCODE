## [Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      bool halvesAreAlike(string s) {
          string a, b;
          int n = s.length();
          for(int i = 0; i < n/2; i++){
              a += s[i];
          }
          for(int i = n/2; i < n; i++){
              b += s[i];
          }
          unordered_map<char, int> mp1, mp2;
          for(auto c: a)
              mp1[c]++;
          for(auto c: b)
              mp2[c]++;
          unordered_map<char, int> mp = {{'a', 1}, {'e', 1}, {'i', 1}, {'o', 1},                                            
                                         {'u', 1}, {'A', 1}, {'E', 1}, {'I', 1},
                                         {'O', 1}, {'U', 1}}; 
          int c1 = 0, c2 = 0;
          for(auto it: mp1){
              if(mp.count(it.first))
                  c1 += it.second;
          }
          for(auto it: mp2){
              if(mp.count(it.first))
                  c2 += it.second;
          }
          cout << c1 << " " << c2;
          return c1 == c2;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      bool halvesAreAlike(string s) {
          int c = 0;
          for(int i = 0; i < s.size(); i++){
              s[i] = tolower(s[i]);
              if(i < s.size()/2){
                  if(s[i] == 97 || s[i] == 101 || s[i] == 105 || s[i] == 111 || s[i] == 117)
                      c++;
              }
              else{
                  if(s[i] == 97 || s[i] == 101 || s[i] == 105 || s[i] == 111 || s[i] == 117)
                      c--;
              }
          }
        return c == 0;
      }
  };
  ```
  
  * 3
  ```cpp
  string vowels = "aeiouAEIOU";
  class Solution {
  public:
      bool halvesAreAlike(string s) {
          int mid = s.size()/2, ans = 0;
          for(int i = 0, j = mid; i < mid; i++, j++){
              if(~vowels.find(s[i])) ans++;
              if(~vowels.find(s[j])) ans--;
          }
          return ans == 0;
      }
  };
  ```

<hr>

* **PYTHON**

  * 1
  ```py
  vowels = "aeiouAEIOU"
  class Solution:
      def halvesAreAlike(self, s: str) -> bool:
          mid, ans = len(s)//2, 0
          for i in range(mid):
              if s[i] in vowels: ans += 1
              if s[mid+i] in vowels: ans -= 1
          return ans == 0
  ```
