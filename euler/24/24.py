#perm_size = 4 if you want the permutations of 0,1,2,3
perm_size = 4

#create list for perms, this will be = [0,1,2,3] if perm_size=4 
p = range(0, perm_size)

sum = []


#recursive function to determine 
def fl(z):
   global total_perms
   while p:
      #total number of perms
      total_perms = reduce(lambda x,y: x*y, range(1, len(p)+1))

      y = total_perms / len(p)
      x = z/y
      print total_perms, len(p),y, x, ':', p[x]

      sum.append(p.remove(p[x]))
      z = z%y


   
