## [Min Stack](https://leetcode.com/problems/min-stack/)

* **C++**
```cpp
class MinStack {
private:
    stack<int> s1;
    stack<int> s2;
    
public:   
    void push(int x) {
        s1.push(x);
        if(s2.empty() || x <= getMin())
            s2.push(x);
    }
    
    void pop() {
        if(s1.top() == getMin())
            s2.pop();
        s1.pop();
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return s2.top();
    }
};
```

* **Python**
```py
class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        s2 = self.s2
        s2.append(x if not s2 else min(x, s2[-1]))

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]
```
