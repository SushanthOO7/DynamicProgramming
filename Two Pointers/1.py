"""Two pointers:
Question 1: Reverse String — LeetCode #344
Input:
s = ["h","e","l","l","o"]

Output:
["o","l","l","e","h"]

"""

s = ["h","e","l","l","o"]
start = 0
end = len(s) - 1
while start < end:
	t = s[start]
	s[start] = s[end]
	s[end] = t
	start += 1
	end -= 1
print(s)