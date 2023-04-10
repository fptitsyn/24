a = open("24_2.txt").readline()
a = a.replace("AB", "*").replace("CB", "*").replace("A", " ").replace("B", " ").replace("C", " ")
s = [x for x in a.split()]
print(len(max(s, key=len)))