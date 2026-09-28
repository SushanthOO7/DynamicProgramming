"""Two pointers:
Question 10 — Valid Palindrome II (LeetCode #680)
Problem Description
Given a string s, return True if the string can become a palindrome after deleting at most one character.
You are also allowed to delete nothing if the string is already a palindrome.

Input
s = "abca"
Expected Output
True
Because you can remove "c":
"aba"
Another Example:
Input:
s = "abc"
Expected Output:
False
You may delete at most one character.
"""
def p(l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        else:
            r -= 1
            l += 1
    return True

s = "abccbca"
l = 0
r = len(s) - 1
flag = True
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        flag = p(l + 1, r) or p(l, r - 1)
        break
print(flag)
