## [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

* **C++**
```cpp
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int res = 0;
        for(int i = 0; i < k; i++)
            res += cardPoints[i];
        
        int curr = res;
        
        for(int i = k - 1; i >= 0; i--)
        {
            curr -= cardPoints[i];
            curr += cardPoints[cardPoints.size() - k + i];
            res = max(res, curr);
        }
        
        return res;
    }
};
```

* **Python**
```py
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = 0
        for i in range(k):
            res += cardPoints[i]
        
        curr = res
        
        for i in range(k-1, -1, -1):
            curr -= cardPoints[i]
            curr += cardPoints[len(cardPoints) - k + i]
            res = max(res, curr)
        
        return res
```
