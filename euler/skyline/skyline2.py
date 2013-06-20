#Efficient Skyline Algorithm that runs near O(n) time vs the typical algorithm which runs O(n)> time. Instead of overwriting an array constantly with rendant writes, we use a sweep line method that only iterates over given points (L).  For each point, if we see a point that has a longer c, we will add a new point in L (a new point consisting of the old point C value as X1 and new c value as X2 (c).   


#coordinates for buildings in 2d: x, y, width
L =  [[1,11,5], [2,6,7], [3,13,9], [12,7,16], [14,3,25],[19,18,22], [23,13,29], [24,4,28]]
E = 0
H = 1
C = 2
#result 
r = []

#initialize
e = L[0][E]
h = L[0][H]
c = L[0][C]
r.extend([e,h])

def addpoint(h, e, c, i):
   if i < len(L)-1:
      while(L[i][E] < e):
         i = i+1
      L.insert(i, [e,h,c])
   else:
      L.append([e,h,c])

i = 1
z = len(L)
while i<z:
   if L[i][E] >= c:
      r.append(c - r[-2])
      #append the flat area in between buildings if exists
      if L[i][E] > c:
         r.extend([c,0,L[i][E]-r[-2]])
      e = L[i][E]
      h = L[i][H]
      c = L[i][C]
      r.extend([e,h])
   elif L[i][H] <= h:
      if L[i][C] > c:
         addpoint(L[i][H], c, L[i][C], i)
         z = z + 1
      #els we skip 
   else: #L[i][H] > h
      r.extend([L[i][E] - r[-2], L[i][E], L[i][H]])
      if L[i][C] < c:
         addpoint(h,L[i][C], c,i) 
         z=z+1
      e = L[i][E]
      h = L[i][H]
      c = L[i][C]
   i = i+1
print r
