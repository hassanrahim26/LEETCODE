## [Image Overlap](https://leetcode.com/problems/image-overlap/)

* **C++**
```cpp
class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        vector<int> v1, v2;
        int n = img1.size();
        unordered_map<int, int> mp;
        
        for(int i = 0; i < n*n; i++){
            if(img1[i/n][i%n] == 1)
                v1.push_back(i/n * 100 + i%n);
            if(img2[i/n][i%n] == 1)
                v2.push_back(i/n * 100 + i%n);   
        }
        
        for(int i: v1)
            for(int j: v2)
                mp[i-j]++;
        
        int ans = 0;
        for(auto it: mp) ans = max(ans, it.second);
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        v1, v2, n = [], [], len(img1)
        mp = collections.Counter()
        
        for i in range(n*n):
            if(img1[i//n][i%n] == 1):
                v1.append(i//n * 100 + i%n)
            if(img2[i//n][i%n] == 1):
                v2.append(i//n * 100 + i%n)
        
        mp = collections.Counter(i - j for i in v1 for j in v2)
        return max(mp.values() or [0])
```
