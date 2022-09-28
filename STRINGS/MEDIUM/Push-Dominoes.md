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
  * 1
    ```py
    class Solution:
        def pushDominoes(self, dominoes: str) -> str:
            d = list(dominoes)
            l = 0
            for r in range(len(d)):
                if(d[r] == '.'):
                    continue
                elif((d[r] == d[l]) or (d[l] == '.' and d[r] == 'L')):
                    for k in range(l, r):
                        d[k] = d[r]
                elif(d[l] == 'R' and d[r] == 'L'):
                    m = (r-l-1)//2
                    for k in range(1, m+1):
                        d[r-k] = 'L'
                        d[l+k] = 'R'
                l = r
        
            if(d[l] == 'R'):
                for k in range(l, len(d)):
                    d[k] = 'R'
        
            return ''.join(d)
    ```
    
  * 2
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
