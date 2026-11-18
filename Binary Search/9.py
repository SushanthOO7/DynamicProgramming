"""
Binary Search
Question 9 — Time Based Key-Value Store
LeetCode #981 — Medium
Problem Description
Design a data structure that stores values for a key at different timestamps.
You need two operations:
set(key, value, timestamp)
Stores value for key at that timestamp.
get(key, timestamp)
Returns the value with the largest stored timestamp ≤ the requested timestamp.
If no such timestamp exists, return "".

Example 1
set("foo", "bar", 1)
set("foo", "bar2", 4)

Stored data:
"foo":
timestamp 1 → "bar"
timestamp 4 → "bar2"
Now:
get("foo", 1)

Output:
"bar"
And:
get("foo", 3)

Output:
"bar"
Because timestamp 1 is the largest timestamp <= 3.
And:
get("foo", 5)

Output:
"bar2"
because timestamp 4 is the largest timestamp <= 5.

Example 2
set("love", "high", 10)
set("love", "low", 20)
get("love", 5)

Output:
""
There is no timestamp <= 5.

Target Complexity
set(): O(1)
get(): O(log n)
"""

class TimeMap:
    def __init__(self):
        self.d = {}
    def set(self, key, value, timestamp):
        self.d.setdefault(key, []).append([value, timestamp])
    def get(self, key, timestamp):
        if key not in self.d:
            return ""
        data = self.d[key]
        value = ""
        l = 0
        r = len(data) - 1
        while l <= r:
            m = (l + r) // 2
            if data[m][1] <= timestamp:
                value = data[m][0]
                l = m + 1
            else:
                r = m - 1
        return value

t = TimeMap()
t.set("foo", "bar", 1)
t.set("foo", "bar2", 4)
s = t.get("foo", 3)
t.set("love", "high", 10)
t.set("love", "low", 20)
a = t.get("love", 5)
print(s)
print(a)