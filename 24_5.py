s = open("24_5.txt").readline()
h = "0123456789ABCDEF"
d = set()
a = [(s[i], i) for i in range(len(s)) if s[i] in h]