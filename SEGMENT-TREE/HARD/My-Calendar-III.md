## [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

* **C++**
```cpp
class MyCalendarThree {
public:
    map<int, int> timeline;    
    MyCalendarThree() {
        
    }
    
    int book(int s, int e) {
        timeline[s]++;
        timeline[e]--;
        int ongoing = 0, k = 0;
        for(pair<int, int> t: timeline)
            k = max(k, ongoing += t.second);
        return k;
    }
};
```

* **PYTHON**
```py
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.timeline = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1
        return max(accumulate(self.timeline.values()))
```
