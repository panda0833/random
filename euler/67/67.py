# basic node class
class node:
   def __init__(self, children, distance):
      self.children = children
      #need this for dijkstra to mark each node
      self.marked = False
      #sum of distances up to this element in the tree, needed for dijkstra
      self.sumd = 0
      self.distance = distance

#this is basically dijkstra's algorithm (which is based off breadth search)
def dijkstra(root):
   #this is our initial Queue, add root to it
   q = [root]
   #need to mark root's sumd as root's distance
   root.sumd = root.distance

   #maxd = max distance 
   maxd = 0

   while q:
      e = q.pop()
      for child in e.children:
         # if child exists
         if child:
            #new child, add to queue and set as marked  
            if child.marked == False:
               q.insert(0,child)
               child.sumd = e.sumd + child.distance
               child.marked = True
            # old node, new path hence we need to check distance
            else:
               if (e.sumd+child.distance) > child.sumd:
                  child.sumd = (e.sumd+child.distance)

            #keep track of largest distance
            if child.sumd > maxd:
               maxd = child.sumd

   print "Max distance is: ", maxd
         

# Uses depth first search to create the tree 
def build_tree(i,k,l):
   #check if are within bounds of the list 
   if i >= len(l):
      return None

   # we could set another variable 'marked' in the node
   # to true, but there is no need since we can check
   # if it's a node or int, node => marked, int => unmarked. 
   # Node was already created by an earlier recursive
   # call, so it's effectively 'marked', hence just return it
   if type(l[i][k]) != int:
      return l[i][k]  
      
   #left child node 
   lc = build_tree(i+1, k, l)
   #right child node 
   rc = build_tree(i+1, k+1, l)

   #children list, list containing lc and rc
   cl = []
   if lc != None and rc != None:
      cl = [lc, rc]

   #create node using children and number value in the list position
   # which is essentially the 'distance' of node to any children nodes
   l[i][k] = node(cl, l[i][k]) 
   
   return l[i][k]


# Unit test, l looks like the following tree:
#     2
#    2 4
#  1  2  3
def test_build_tree():
   l = [[2], [2,4],[1,2,3] ]
   tree = build_tree(0,0,l)

   #debug: print l
   roots_children = tree.children

   failed = False

   if roots_children[0].distance != 2 or roots_children[1].distance != 4:
      print "Failed Root's children test"
   else:
      print "Passed Root's children test"

   #roots children's children
   rcc1 = roots_children[0].children
   rcc2 = roots_children[1].children

   if rcc1[0].distance != 1 or rcc1[1].distance != 2 or rcc2[0].distance != 2 or rcc2[1].distance != 3:
      print "Failed root's children's children test"
   else:
      print "Passed root's children's children test"


   
      
# Unit test, l looks like the following tree:
#     2
#    2 4
#  1  2  3
# hence sample distances for leaf nodes starting from left leaf should be:
# 5, 6, 8, 9  respectively 
def test_dijkstra():
   l = [[2], [2,4],[1,2,3] ]
   i = 0 
   k= 0
   tree = build_tree(i,k,l)
   dijkstra(tree)

   if tree.children[0].children[0].sumd == 5 and tree.children[1].children[0].sumd == 8 and tree.children[1].children[1].sumd == 9:
      print "Passed all sample distances"
   else:
      print "Failed one or more sample distances"






   


