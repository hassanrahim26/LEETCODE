## [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)

* **C++**
```cpp
class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> m = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        unordered_set<string> st;
        for(auto w: words){
            string s;
            for(auto c: w)
                s += m[c - 'a'];
            st.insert(s);
        }
        return st.size();
    }
};
```

* **Python**
```py
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        
        st = set()
        for w in words:
            s = ""
            for c in w:
                s += m[ord(c) - ord('a')]
            st.add(s)
            
        return len(st)
```
