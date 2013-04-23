f = open("input.txt", "r+")
x = f.readlines()
for y in x:
   d = []
   for q in range(0, len(y), 3):
      d.append(int(y[q]+y[q+1]))
   p.append(d)

