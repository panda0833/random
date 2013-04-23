import re
#parse file into list
l = []
f = open("input", "r")
x = f.readline()
while x:
   l.append(map(lambda x: int(x), re.findall('\d\d', x)))
   x = f.readline()

