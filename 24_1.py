a = open("24_1.txt").readline()
a = a.replace("XX", "X X").replace("YY", "Y Y").replace("ZZ", "Z Z")
a = a.replace("XY", "X Y").replace("YX", "Y X").replace("ZX", "Z X")
a = a.replace("XZ", "X Z").replace("YZ", "Y Z").replace("ZY", "Z Y")
s = [x for x in a.split()]
print(len(max(s, key=len)))
