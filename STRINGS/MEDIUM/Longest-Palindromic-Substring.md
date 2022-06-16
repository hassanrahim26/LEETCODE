## [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

* **C++**
```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.length() == 0 || s.length() == 1)        
            return s;
        
        int maxLenBeginIndex = 0, maxLen = 1, mid = 0;
        
        while(mid < s.length()){
            int midBegin = mid, midEnd = mid;
            
            while(midEnd + 1 < s.length() && s[midEnd] == s[midEnd + 1]){
                midEnd++;
            }
            
            mid = midEnd + 1;
            int leftWindow = midBegin, rightWindow = midEnd;
            
            while(leftWindow - 1 >= 0 && rightWindow + 1 < s.length() && s[leftWindow - 1] == s[rightWindow + 1]){
                leftWindow--;
                rightWindow++;
            }
            
            int currLen = rightWindow - leftWindow + 1;
            if( currLen  > maxLen ){
                maxLenBeginIndex = leftWindow;
                maxLen = currLen;
            }
        }
        
        return s.substr(maxLenBeginIndex, maxLen);
    }
};
```
