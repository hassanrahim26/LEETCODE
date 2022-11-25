## [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)

* **C++**
```cpp
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        int n = arr.size();
        vector<int> left(n,-1), right(n, n);
        stack<int> st;
        
        for(int i = 0; i < n; i++){
            while(st.size() and arr[i] < arr[st.top()]) st.pop();
            if(st.size())
                left[i] = i - st.top();
            else
                left[i] = i+1;
            st.push(i);
        }
        
        while(st.size()) st.pop();
        
        for(int i = n-1; i >= 0; i--){
            while(st.size() and arr[i] <= arr[st.top()]) st.pop();
            if(st.size())
                right[i] = st.top() - i;
            else
                right[i] = n-i;
            st.push(i);
        }
        
        int ans = 0, mod = 1e9+7;
        for(int i = 0; i < n; i++){
            long long p = (left[i] * right[i]) % mod;
            p = (p * arr[i]) % mod;
            ans = (ans + p) % mod;
        }
        
        return ans % mod;
    }
};
```
