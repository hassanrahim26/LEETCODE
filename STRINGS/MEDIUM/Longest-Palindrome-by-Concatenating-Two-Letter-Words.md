## [Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)

* **C++**
```cpp
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        int mp[26][26] = {};
        int ans = 0;
        for(auto w: words){
            int a = w[0] - 'a', b = w[1] - 'a';
            if(mp[b][a]){
                ans += 4;
                mp[b][a]--;
            }
            else
                mp[a][b]++;
        }
        for(int i = 0; i < 26; i++){
            if(mp[i][i]){
                ans += 2;
                break;
            }
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mp, ans = [[0] * 26 for _ in range(26)], 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if mp[b][a]:
                ans += 4
                mp[b][a] -= 1
            else:
                mp[a][b] += 1
        
        for i in range(26):
            if mp[i][i]:
                ans += 2
                break
        return ans         
```
