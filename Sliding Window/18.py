"""
Sliding Window:
Question 18 — Maximize the Confusion of an Exam
LeetCode #2024 — Medium
Problem Description
You're given a string answerKey containing only:
'T' and 'F' and an integer k.
You can change at most k characters:
T → F
or
F → T
Return the maximum number of consecutive identical answers you can create.

Example 1
Input:
answerKey = "TTFF"
k = 2

Expected Output:
4

Change both Fs to Ts:
TTFF
  ↓↓
TTTT

Example 2
Input:
answerKey = "TFFT"
k = 1

Expected Output:
3

For example, change one T:
TFFT
↓
FFFT

giving 3 consecutive Fs.
Example 3
Input:
answerKey = "TTFTTFTT"
k = 1

Expected Output:
5

Target Complexity
Time: O(n)
Space: O(1)
"""
answerKey = "TTFTTFTT"
k = 1
l = 0
t = 0
f = 0
m = 0
for r in range(len(answerKey)):

    if answerKey[r] == 'T':
        t += 1
    else:
        f += 1
    while min(t, f) > k:
        v = answerKey[l]
        if v == 'T':
            t -= 1
        else:
            f -= 1
        l += 1
    m = max(m, r - l + 1)

print(m)