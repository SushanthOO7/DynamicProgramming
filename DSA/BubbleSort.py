a = [6, 2, 5, 1, 9, 3, 4]
n = len(a)
for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j+ 1], a[j]
print(a)