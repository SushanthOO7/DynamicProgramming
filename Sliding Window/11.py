"""
Sliding Window:
Question 10 — Fruit Into Baskets
LeetCode #904 — Medium
Problem Description
You are given an integer array fruits, where fruits[i] represents the type of fruit at position i.

You have two baskets. Each basket can hold only one type of fruit, but can hold unlimited fruit of that type.

Starting from some position, you must pick one fruit from every consecutive tree until you encounter a fruit that cannot fit into either basket.

Return the maximum number of fruits you can collect.

In simpler terms:
Find the longest contiguous subarray containing at most 2 distinct numbers.

Example 1
Input:
fruits = [1, 2, 1]

Expected Output:
3
The entire array contains only two types:
1 and 2

Example 2
Input:
fruits = [0, 1, 2, 2]

Expected Output:
3

The longest valid section is:
[1, 2, 2]
It contains only two fruit types.

Example 3
Input:
fruits = [1, 2, 3, 2, 2]

Expected Output:
4
Longest valid window:
[2, 3, 2, 2]
Only fruit types 2 and 3.
Target Complexity
Time: O(n)
Space: O(1) relative to the two fruit types.
Hint
Think about Question 1 — Longest Substring Without Repeating Characters.
Maintain a window:
[1, 2, 3, 2, 2]
 ↑        ↑
 l        r

"""

fruits = [1, 2, 3, 2, 2]
l = 0
d = {}
m = 0
for r in range(len(fruits)):
    d[fruits[r]] = d.get(fruits[r], 0) + 1
    while len(d) > 2:
        o = fruits[l]
        d[o] -= 1
        if d[o] == 0:
            del d[o]
        l += 1
    m = max(m, r - l + 1)
print(m)