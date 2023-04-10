a = open("24_3.txt").readline()
a = a.replace("O", "A").replace("D", "C").replace("F", "C")
a = a.replace("CAA", "*").replace("CCA", "*")
a = a.replace("C", " ").replace("A", " ")
s = [x for x in a.split()]
print(len(max(s, key=len)))

