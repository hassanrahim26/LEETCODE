## [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/)

* **C++**
  * 1
    ```cpp
    class Solution {
    public:
        int minSetSize(vector<int>& arr) {
            int ans = 0, c = 0;
            unordered_map<int, int> mp;
            for(auto x: arr)
                mp[x]++;
        
            vector<int> v;
            for(auto it: mp)
                v.push_back(it.second);
        
            if(v.size() == 1)
                return 1;
            sort(v.begin(), v.end());
            for(int i = v.size()-1; i >= 0; i--){
                if(ans >= arr.size()/2)
                    return c;
                c++;
                ans += v[i];
            }
            return 0;
        }
    };
    ```
    
  * 2
    ```cpp
    class Solution {
    public:
        int minSetSize(vector<int>& arr) {
            int x = 0, ans = 0;
            unordered_map<int, int> mp;
            for(auto i: arr)
                mp[i]++;
        
            priority_queue<int> pq;
            for(auto i: mp)
                pq.push(i.second);
        
            while(x < arr.size()/2){
                x += pq.top();
                pq.pop();
                ans++;
            }
            return ans;
        }
    };
    ```
    
