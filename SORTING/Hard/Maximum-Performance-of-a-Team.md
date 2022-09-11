## [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

* **C++**
```cpp
class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        int mod = 1e9 + 7;
        vector<pair<int, int>> candidates(n);
        for(int i = 0; i <  n; i++)
            candidates.push_back({efficiency[i], speed[i]});
        
        sort(candidates.rbegin(), candidates.rend());
        long speedSum = 0, ans = 0;
        priority_queue<int, vector<int>, greater<int>> pq;
        
        for(auto& [e, s]: candidates){
            pq.push(s);
            speedSum += s;
            
            if(pq.size() > k){
                speedSum -= pq.top();
                pq.pop();
            }
            
            ans = max(ans, speedSum * e);
        }
        return ans % mod;
    }
};
```

* **PYTHON**
```py
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = zip(efficiency, speed)
        candidates = sorted(candidates, key = lambda x: x[0], reverse = True)
        
        speedSum, ans, heap = 0, 0, []
        
        for e, s in candidates:
            heapq.heappush(heap, s)
            speedSum += s
            
            if(len(heap) > k):
                speedSum -= heapq.heappop(heap)
            ans = max(ans, speedSum * e)
        
        return ans % (10**9 + 7)    
```
