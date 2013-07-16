#coordinates for buildings in 2d: x, y, width
buildings =  [[1,11,5], [2,6,7], [3,13,9], [12,7,16], [14,3,25], [19,18,22], [23,13,29], [24,4,28]]

array = [] 

#initialize to max elements  * 2 (max element will likely be in the last field) 
for i in range(buildings[len(buildings)-1][2]*2):
   array.append(0)

for x in buildings:
   #use x range since we don't need to access every value 
   for y in xrange(x[0], x[2]):
      print y,
      if array[y] < x[1]:
         array[y] = x[1]
   
#now we have a list of all the height values
p = [1,array[1]]
for x in range(1, len(array)):
   if p[-1] != array[x]:
      p.append(x-p[-2])
      p.append(x)
      p.append(array[x])

