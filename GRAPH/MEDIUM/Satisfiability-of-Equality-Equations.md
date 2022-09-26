## [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

* **C++**
```cpp
class Solution {
public:
    int uf[26];
    int find(int x){
        if(x != uf[x])    
            uf[x] = find(uf[x]);
        return uf[x];
    }
    bool equationsPossible(vector<string>& equations) {
        for(int i = 0; i < 26; i++){
            uf[i] = i;
        }
        for(string e: equations){
            if(e[1] == '=')
                uf[find(e[0] - 'a')] = find(e[3] - 'a');
        }
        for(string e: equations){
            if(e[1] == '!' and find(e[0] - 'a') == find(e[3] - 'a'))
                return false;
        }
        return true;
    }
};
```

* **PYTHON**
```py
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        uf = [None]*26
        for i in range(26):
            uf[i] = i
            
        for e in equations:
            if(e[1] == '='):
                uf[find(ord(e[0]) - ord('a'))] = find(ord(e[3]) - ord('a'))
        
        for e in equations:
            if(e[1] == '!' and find(ord(e[0]) - ord('a')) == find(ord(e[3]) - ord('a'))):
                return False
        
        return True
```
