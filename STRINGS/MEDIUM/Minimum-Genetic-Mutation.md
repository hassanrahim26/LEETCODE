## [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

* **C++**
```cpp
class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        unordered_set<string> st{bank.begin(), bank.end()};
        if(!st.count(end))  return -1;
        queue<string> q;
        q.push(start);
        
        int ans = 0, n;
        string cur, s;
        
        while(!q.empty()){
            n = q.size();
            while(n--){
                cur = q.front();
                q.pop();
                if(cur == end)  return ans;
                st.erase(cur);
                
                for(int i = 0; i < 8; i++){
                    s = cur;
                    s[i] = 'A';
                    if(st.count(s)) q.push(s);
                    s[i] = 'C';
                    if(st.count(s)) q.push(s);
                    s[i] = 'G';
                    if(st.count(s)) q.push(s);
                    s[i] = 'T';
                    if(st.count(s)) q.push(s);
                }
            }
            ans++;
        }
        return -1;
    }
};
```
