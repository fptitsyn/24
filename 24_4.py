a = open("24_4.txt").readline()

# k = 0
# kmin = 1000000000
# dot = 0
#
# for i in range(len(a)):
#     if a[i] == ".":
#         dot += 1
#     if dot == 7:
#         print(k)
#         kmin = min(kmin, k)
#         k = 0
#         dot = 0
#     k += 1
#
# print(kmin)

s = [x for x in range(len(a)) if a[x] == "."]
s = [s[i + 6] - s[i] + 1 for i in range(len(s) - 6)]
print(min(s))
