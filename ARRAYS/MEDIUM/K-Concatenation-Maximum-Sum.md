## [K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)

* **C++**
```cpp
class Solution {
public:
    int kadane(vector<int>& arr, bool check){
        long long mod = 1000000007;
        int n = arr.size(), cSum = INT_MIN, mSum = INT_MIN;
        
        for(int i = 0; i < (check ? 2 : 1); i++){
            for(int j = 0; j < n; j++){
                if(cSum >= 0)
                    cSum += arr[j];
                else
                    cSum = arr[j];
                mSum = max(mSum, cSum);
                cSum %= mod;
                mSum %= mod;
            }
        }
        return mSum;
    }
    
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        long long mod = 1000000007;
        if(k == 1)
            return kadane(arr, false);
        long long sum = (accumulate(arr.begin(), arr.end(), 0))%mod;
        long long ans = 0;
        
        if(sum >= 0){
            ans = ((kadane(arr,true)) + (((k-2)*sum)%mod))%mod;
        }
        else{
            ans = kadane(arr, true);
        }
        if(ans < 0)
            return 0;
        return ans;
    }
};
```
