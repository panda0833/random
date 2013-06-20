# function to determine the zth value of a permutation (in order)
# based on the perm size 's' 
# ex: s = 3 if you want the permutations of 0,1,2 which would be:
# 012, 021, 102, 120, 201, 210 
def fl(z, s):
   #create list for perms, this will be = [0,1,2] if s=4 
   p = range(0, s)

   #resulting value 
   result = []

   while p:
      #total number of perms
      total_perms = reduce(lambda x,y: x*y, range(1, len(p)+1))

      #divide total perms by total number of perms 
      y = total_perms / len(p)
      x = z/y
      result.append(p[x])
      p.remove(p[x])
      z = z%y

   return reduce(lambda x,y: str(x)+str(y),result)

def test_fl(): 
   #perm_size = 4 if you want the permutations of 0,1,2,3
   perm_size = 3

   #we want the 3rd value of this permutation which should be 102
   #3rd value starting from 0 index, hence '2nd' value
   if fl(2, perm_size) == '102':
      print "Test passed"
   else:
      print "Test failed"
   


   

