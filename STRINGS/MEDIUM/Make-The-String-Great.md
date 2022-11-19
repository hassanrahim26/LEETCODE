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
