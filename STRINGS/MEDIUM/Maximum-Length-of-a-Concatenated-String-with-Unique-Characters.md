## [Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

* **C++**
```cpp
class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<string> unique = {""};
        int ans = 0;
        for(int i = 0; i < arr.size(); i++){
            for(int j = 0; j < unique.size(); j++){
                string x = arr[i] + unique[j];
                set<int> st(x.begin(), x.end());
                if(x.size() == st.size()){
                    unique.push_back(x);
                    ans = ans > x.size() ? ans : x.size();
                }
            } 
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = ['']
        ans = 0
        for i in range(len(arr)):
            for j in range(len(unique)):
                x = arr[i] + unique[j]
                if len(x) == len(set(x)):
                    unique.append(x)
                    ans = max(ans, len(x))
                    
        return ans
```
