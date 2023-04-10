import string
a = open("24-186.txt").readline()
k = 0
c = 0
for i in range(len(a) - 11):
    if a[i] == "7" and a[i - 1] in string.ascii_uppercase:
        for j in range(i, i + 11):
            if a[j] in "0123456789":
                c += 1
        if c == 11:
            if (int(a[i]) + int(a[i + 1])) == (int(a[i + 9]) + int(a[i + 10])):
                k += 1
        c = 0

print(k)
