"""
Sliding Window:
Question 8 — Permutation in String
LeetCode #567 — Medium
Problem Description
You are given two strings s1 and s2.
Return True if s2 contains any permutation of s1 as a contiguous substring. Otherwise, return False.
A permutation contains exactly the same characters with the same frequencies, but they can appear in any order.

Example 1
Input:
s1 = "ab"
s2 = "eidbaooo"

Expected Output:
True

Why? "ba" appears inside s2:
e i d b a o o o
      └─┬─┘
       "ba"

"ba" is a permutation of "ab".

Example 2
Input:
s1 = "ab"
s2 = "eidboaoo"

Expected Output:
False
There is no contiguous substring containing exactly one a and one b.

Example 3
Input:
s1 = "adc"
s2 = "dcda"

Expected Output:
True

Because:
"cda" is a permutation of "adc".
Target Complexity
Aim for:
Time:  O(n)
Space: O(1)
Since the strings contain lowercase English letters, at most 26 character counts are needed.
"""

s1 = "ab"
s2 = "eidbaooo"


