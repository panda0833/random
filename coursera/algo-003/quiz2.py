def quicks(a, l, r):
   global comp
   #base case, if right - left indexs <= 1 then we return since size of array is <= 1
   if r-l <= 1:
      return a

   comp = comp + r-l-1
   p = partitionm(a, l, r)
   quicks(a,l,p-1)
   quicks(a,p,r)
   return a


def partitionm(a, l, r):
   mid = ((r-l)-1)/2
   li = [a[l],a[l+mid], a[r-1]] 
   li.sort()
   if li[1] == a[l]:
      temp3= l
   elif li[1] == a[l+mid]:
      temp3= l+mid
   else:
      temp3= r-1
   temp2 = a[l]
   a[l] = a[temp3]
   a[temp3] = temp2
   p = a[l]
   i = l + 1
   for j in range(l+1,r):
      if a[j] < p:
         temp = a[j]
         a[j] = a[i]
         a[i] = temp
         i = i + 1
   temp = a[l]
   a[l] = a[i-1]
   a[i-1] = temp
   return i
   

def partitionlp(a, l, r):
   #use last as pivot element
   p = a[r-1]
   temp = a[l]
   a[l] = a[r-1]
   a[r-1] = temp
   i = l + 1
   for j in range(l+1,r):
      if a[j] < p:
         temp = a[j]
         a[j] = a[i]
         a[i] = temp
         i = i + 1
   temp = a[l]
   a[l] = a[i-1]
   a[i-1] = temp
   return i

def partition(a, l, r):
   p = a[l]
   i = l + 1
   for j in range(l+1,r):
      if a[j] < p:
         temp = a[j]
         a[j] = a[i]
         a[i] = temp
         i = i + 1
   temp = a[l]
   a[l] = a[i-1]
   a[i-1] = temp
   return i



   
