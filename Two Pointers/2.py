"""Two pointers:
Question 2 — Valid Palindrome
Input:  "racecar"
Output: True

Input:  "hello"
Output: False

Input:  "abba"
Output: True
"""

s = "racecar"
start = 0
end = len(s) - 1
flag = True
while start < end:
	if s[start] != s[end]:
		flag = False
		break
	else:
		start += 1
		end -= 1
print(flag)