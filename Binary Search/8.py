"""
Binary Search
Question 8 — Capacity to Ship Packages Within D Days
LeetCode #1011 — Medium ⭐
Problem Description
You have packages with weights:
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
The packages must be shipped in the given order.
A ship has some capacity C. Each day, you load packages in order until adding the next package would exceed the capacity. Then that package goes to the next day.
Return the minimum ship capacity needed to ship everything within days.
Example 1
Input:
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

Expected Output:
15
With capacity 15:
Day 1: 1 + 2 + 3 + 4 + 5 = 15
Day 2: 6 + 7 = 13
Day 3: 8
Day 4: 9
Day 5: 10
Everything ships within 5 days. ✅

Example 2
weights = [3,2,2,4,1,4]
days = 3

Expected:
6
One valid schedule:
Day 1: 3 + 2 = 5
Day 2: 2 + 4 = 6
Day 3: 1 + 4 = 5

Hint:
What are we binary searching?
We're searching for the capacity, just like Koko searched for the eating speed.
Think about the possible capacities:
too small                 large enough
❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅
              ↑
       minimum capacity
Once some capacity works, every larger capacity also works.
What should l and r be?
Think about these carefully.
The smallest possible capacity can't be smaller than the heaviest individual package:
l = max(weights)
Why? If there's a package weighing 10, a ship with capacity 9 can never carry it.
The largest capacity we would ever need is enough to ship everything in one day:
r = sum(weights)
So:
max(weights) <= answer <= sum(weights)
Your task
For each candidate capacity:
m = (l + r) // 2
simulate shipping and calculate:
How many days would capacity m require?
Then:
required_days <= days
→ capacity works
→ try SMALLER capacity
required_days > days
→ capacity too small
→ try LARGER capacity

Aim for:
Time: O(n log(sum(weights)))
Space: O(1)
"""

weights = [3,2,2,4,1,4]
days = 3

l = max(weights)
r = sum(weights)
total_weight = r
res = r
def days_taken(max_capacity):
    day = 1
    s = 0
    for w in weights:
        if s + w > max_capacity:
            s = 0
            day += 1
        s += w
    return day
while l <= r:
    m = (l + r) // 2
    total_days = days_taken(m)
    if total_days <= days:
        res = min(res, m)
        r = m - 1
    else:
        l = m + 1
print(res)

