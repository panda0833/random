import math

#sample imput data
D = []
#our heap, stored as an array
H = [None]
#next empty space in the heap
N = 0

def insert(x):
   global N 
   H[N] = x
   bubble_up(N)
   N = N + 1
   H.append(None)
   print_heap()

def getMin(x):
   x = H[0]
   H[0] = H[N]
   H[N] = None
   bubble_down(0)
   --N
   return x
   
def bubble_down(n):
   k = n*2
   #base case
   if k > N:
      return
   x = None
   if k+1 > N:
      if H[n] > H[k]:
         x = k
         swap(n, k)
   else:
      if H[n] > max(H[k], H[k+1]):
         if H[k] > H[k+1]:
            x = k+1
            swap(n, k+1)
         else:
            x = k
            swap(n,k)
   bubble_down(x)
         
def swap(n, k):
   t = H[k+1]
   H[k+1] = H[n]
   H[n] = t

#bubble  up or 'heapify'
def bubble_up(n):
   #no need to get floor, since int values automatically get floor
   v =n/2
   if H[n] < H[v]:
      #swap h[v] with h[n]
      t = H[v]
      H[v] = H[n]
      H[n] = t
      bubble_up(v)
      


#takes O(N) time 
def print_heap():
   i = 0 
   p = 1
   f = 0
   size = len(H)
   #calculate closest 2 power of heap's size
   tmp = int(math.log(size)/math.log(2))+1
   #we will go at each level (p) and print only the
   #elements at that level.  
   while p <= tmp:
   	s0 = 2**(tmp-f)
   	print '-' * s0,
   	a = 2**(tmp-f+1)-3
   	while i < 2**p-1 and i < size:
   	   print H[i],'-'*a,
   	   i = i + 1
   	print ''
   	p = p + 1
   	f = f + 1
	
