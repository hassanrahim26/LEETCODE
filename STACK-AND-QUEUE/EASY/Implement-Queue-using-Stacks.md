## [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

* **C++**
```cpp
class MyQueue {
    stack<int> s1;
    stack<int> s2;
public:
    MyQueue() {
        s1 = stack<int>();
        s2 = stack<int>();
    }
    
    void push(int x) {
        while(!s1.empty())
        {
            s2.push(s1.top());
            s1.pop();
        }
        
        s2.push(x);
        while(!s2.empty())
        {
            s1.push(s2.top());
            s2.pop();
        }
    }
    
    int pop() {
        int temp = s1.top();
        s1.pop();
        return temp;
    }
    
    int peek() {
        return s1.top();
    }
    
    bool empty() {
        return s1.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```

* **PYTHON**
```py
class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if(self.s2 == []):
            while(self.s1 != []):
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return self.s1 == [] and self.s2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
