#basic node class
class node:
   def __init__(self, child_edges):
      self.child_edges = child_edges 
      self.marked = False
      #sum of distances up to this element in the tree, needed for dijkstra
      self.sumd = 0

#using an edge class defined below has a side effect that we can  only traverse from root to bottom (leaves) but we cannot traverse the opposite way (leaves to root).  We would have to add another variable (parent) to the class and then assign it each time.  For this application we don't need that functionality, hence i'm leaving it out.  
class edge:
   def __init__(self, node, distance):
      self.node = node
      self.distance = distance

#this is basically dijkstra's algorithm (which is based off breadth search)
def dijkstra(root_edge):
   #this is our initial Queue, add root to it
   q = [root_edge.node]
   #need to mark root's sumd as root's distance
   root_edge.node.sumd = root_edge.distance

   #maxd = max distance or largest distance 
   maxd = 0

   while q:
      e = q.pop()
      for edge in e.child_edges:
         # if edge to node exists
         if edge.node:
            #new node, add to queue and set as marked  
            if edge.node.marked == False:
               q.insert(0,edge.node)
               edge.node.sumd = e.sumd + edge.distance
               edge.node.marked = True
            # old node, new path hence we need to check distance
            else:
               if edge.node.sumd > e.sumd+edge.distance:
                  edge.node.sumd = e.sumd+edge.distance

            #keep track of largest distance
            if edge.node.sumd > maxd:
               maxd = edge.node.sumd

   print "Maxd is: ", maxd
         
#use depth search to build the tree from the input file list 
#Arguments:l = list to build tree from,
#i = index to depth of tree, k = position within depth  
def build_tree(i, k, l):
   if i >= len(l):
      return None

   #recurse for child edges 
   a_edge = build_tree(i+1, k, l)
   b_edge = build_tree(i+1, k+1, l)
   child_edges = [] 
   #this node
   x = None

   if a_edge != None and b_edge != None:
      child_edges = [a_edge, b_edge]

   x = node(child_edges)

   return edge(x, l[i][k]) 

# Unit test, l looks like the following tree:
#     2
#    2 4
#  1  2  3
def test_build_tree():
   l = [[2], [2,4],[1,2,3] ]
   i = 0 
   k= 0
   tree = build_tree(i,k,l)
   
   roots_children = tree.node.child_edges

   failed = False

   if roots_children[0].distance != 2 or roots_children[1].distance != 4:
      print "Failed Root's children test"
   else:
      print "Passed Root's children test"

   #roots children's children
   rcc1 = roots_children[0].node.child_edges
   rcc2 = roots_children[1].node.child_edges

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

   if tree.node.child_edges[0].node.child_edges[0].node.sumd == 5 and tree.node.child_edges[0].node.child_edges[1].node.sumd == 6 and tree.node.child_edges[1].node.child_edges[0].node.sumd == 8 and tree.node.child_edges[1].node.child_edges[1].node.sumd == 9:
      print "Passed all sample distances"
   else:
      print "Failed one or more sample distances"






   


