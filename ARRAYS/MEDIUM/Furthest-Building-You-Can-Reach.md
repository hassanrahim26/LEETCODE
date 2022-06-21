## [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)

* **C++**
```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& h, int b, int l) {
        priority_queue<int> pq;
        for(int i = 0; i < h.size() - 1; i++)
        {
            int x = h[i+1] - h[i];
            if(x > 0)
                pq.push(-x);
            if(pq.size() > l)
            {
                b += pq.top();
                pq.pop();
            }
            if(b < 0)
                return i;
        }
        
        return h.size() - 1;
    }
};
```

* **Python**
```py
class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        heap = []
        for i in range(len(h) - 1):
            x = h[i+1] - h[i]
            if x > 0:
                heapq.heappush(heap, x)
            if len(heap) > l:
                b -= heapq.heappop(heap)
            if b < 0:
                return i
        return len(h) - 1
```
