def find_inversion(n):
   if len(n) <= 1:
      return n

   size = len(n)/2
   ls = n[:size]
   rs = n[size:]

   ls = find_inversion(ls)
   rs = find_inversion(rs)

   return sc(ls, rs)
   

def mergeSort(a):
   #our stop conditions for recursion
   if len(a) <= 1:
      return a

   size = len(a)/2
   #recursivly divide the problem into two halves
   left_side = a[:size]
   right_side = a[size:]
   
   ls = mergeSort(left_side)
   rs = mergeSort(right_side)

   return merge(ls, rs)
   

def merge(lef, rig):
   merged = []
   while lef and rig:
      if lef[0] < rig[0]:
         merged.append(lef.pop(0))
      else:
         merged.append(rig.pop(0))

   if lef:
      merged.extend(lef)
   elif rig:
      merged.extend(rig)
   
   return merged


      
def sc(lef, rig):
   global count
   merged = []
   while lef and rig:
      if lef[0] < rig[0]:
         merged.append(lef.pop(0))
      else:
         merged.append(rig.pop(0))
         count+= len(lef)
   if lef:
      merged.extend(lef)
   elif rig:
      merged.extend(rig)
      ++count

   return merged

