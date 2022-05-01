## [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)

* **C++**
```cpp
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int low = 0, high = position.back() - position.front();
        
        while(low < high)
        {
            int mid = high - (high - low)/2;
            
            if(count(position, mid) >= m)
                low = mid;
            else
                high = mid - 1;
        }
        
        return low;
    }
    
private:
    int count(vector<int>& position, int d){
        int ans = 1, cur = position[0];
        
        for(int i = 1; i < position.size(); i++){
            
            if(position[i] - cur >= d){
                ans++;
                cur = position[i];
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(d):
            ans, cur = 1, position[0]
            
            for i in range(n):
                if position[i] - cur >= d:
                    ans += 1
                    cur = position[i]
            
            return ans
        
        low, high = 0, position[-1] - position[0]
        
        while low < high:
            mid = high - (high - low)//2
            
            if count(mid) >= m:
                low = mid
            else:
                high = mid - 1
        
        return low
```
