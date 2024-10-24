a = [0]
length = int(input("Please enter the length\n"))

for k in range(1, length):
    if a[k - 1] - k > 0 and a[k - 1] - k not in a:
        a.append(a[k - 1] - k)
    else:
        a.append(a[k - 1] + k)

print(a)