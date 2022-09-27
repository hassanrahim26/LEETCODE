## [Push Dominoes](https://leetcode.com/problems/push-dominoes/)

* **C++**
```cpp
class Solution {
public:
    string pushDominoes(string d) {
        int l = 0;
        for(int r = 0; r < d.size(); r++){
            if(d[r] == '.'){
                continue;
            }
            else if((d[r] == d[l]) || (d[l] == '.' and d[r] == 'L')){
                for(int k = l; k < r; k++)
                    d[k] = d[r];
            }
            else if(d[l] == 'R' and d[r] == 'L'){
                int m = (r - l - 1)/2;
                for(int k = 1; k <= m; k++)
                    d[r-k] = 'L', d[l+k] = 'R';
            }
            l = r;
        }
        if(d[l] == 'R'){
            for(int k = l; k < d.size(); k++)
                d[k] = 'R';
        }
        return d;
    }
};
```

* **PYTHON**
```py
class Solution:
    def pushDominoes(self, d: str) -> str:
        s = ''
        while d != s:
            s = d
            d = d.replace('R.L', 'xxx')
            d = d.replace('R.', 'RR')
            d = d.replace('.L', 'LL')
        return d.replace('xxx', 'R.L')
        
```
