## [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

```cpp
class MyCircularQueue {
private:
    vector<int> q;
    int cnt, sz, headIdx;
    
public:
    MyCircularQueue(int k) {
        q.resize(k); // the queue holding the elements for the circular queue
        cnt = 0; // the number of elements in the circular queue
        sz = k; // size of queue
        headIdx = 0;
    }
    
    bool enQueue(int value) {
        if(isFull())  return false;
        q[(headIdx + cnt) % sz] = value;
        cnt += 1;
        return true;
    }
    
    bool deQueue() {
        if(isEmpty())   return false;
        headIdx = (headIdx + 1) % sz;
        cnt -= 1;
        return true;
    }
    
    int Front() {
        if(isEmpty())   return -1;
        return q[headIdx];
    }
    
    int Rear() {
        if(isEmpty())   return -1;
        return q[(headIdx + cnt - 1) % sz];
    }
    
    bool isEmpty() {
        return cnt == 0;    
    }
    
    bool isFull() {
        return cnt == sz;    
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
```
