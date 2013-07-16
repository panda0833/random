import math
i = 0 
p = 1
l = [1,1, 2, 3, 4, 5, 6,1, 2, 3, 4, 5, 6, 7, 8, 0, 2, 4]
f = 0
tmp = int(math.log(len(l))/math.log(2))+1
while p <= tmp:
   s0 = 2**(tmp-f)
   print '-' * s0,
   a = 2**(tmp-f+1)-3
   while i < 2**p-1 and i < len(l):
      print l[i],'-'*a,
      i = i + 1
   print ''
   p = p + 1
   f = f + 1
 
