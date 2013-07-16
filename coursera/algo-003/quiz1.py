def mergeSort(a):
   size = len(a)/2
   #our stop conditions for recursion
   if size == 1:
      return a

   #recursivly divide the problem into two halves
   left_side = a[:len(a)/2]
   right_side = a[len(a)/2:]
   
   mergeSort(left_side)
   mergeSort(right_side)

   return merge(left_side, right_side)
   

def merge(lef, rig):
   merged = []
   while 
   for x in range(1, len(rig)):
   
