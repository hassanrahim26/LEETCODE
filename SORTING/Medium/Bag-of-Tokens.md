## [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

* **C++**
```cpp
class Solution {
public:
    int bagOfTokensScore(vector<int>& t, int p) {
        sort(t.begin(), t.end());
        int l = 0, r = t.size() - 1;
        int cur_score = 0, max_score = 0;
        
        while(l <= r){
            if(t[l] <= p){
                p -= t[l];
                cur_score += 1;
                max_score = max(max_score, cur_score);
                l += 1;
            }
            else if(cur_score >= 1){
                p += t[r];
                cur_score -= 1;
                r -= 1;
            }
            else{
                break;
            }
        }
        return max_score;
    }
};
```

* **PYTHON**
```py
class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        t.sort()
        l, r, cur_score, max_score = 0, len(t) - 1, 0, 0
        
        while(l <= r):
            if(t[l] <= p):
                p -= t[l]
                cur_score += 1
                max_score = max(max_score, cur_score)
                l += 1
            elif(cur_score >= 1):
                p += t[r]
                cur_score -= 1
                r -= 1
            else:
                break
                
        return max_score
```
