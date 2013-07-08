hashmap = dict({})

def find(x):
   if x == 1:
      return 1
   if not hashmap.get(x):
      n = 0 
      if x%2 == 0:
         n = x / 2 
      else:
         n = 3 * x + 1 
      hashmap.update({x: 1+find(n)})
   return hashmap.get(x)

a = range(800000, 999999)
a.reverse()

maxx = (0,0)
for x in a:
   if find(x) > maxx[1]:
      maxx = (x, find(x))
      print x, find(x)

      
