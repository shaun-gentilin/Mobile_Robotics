import random, math
from PIL import Image
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

#sample a vertex uniformly and randomly from
# the vertex set of the of the occupancy map M
def sampleVertex():
    #get the vertex set V from the occupancy grid
    V = []
    for i in range(len(M)):
        for j in range(len(M[0])):
            V.append((j,i))
    return random.choice(V)

#euclidean distance between two vectors v1 and v2
def d(v1, v2):
    x1, y1, x2, y2 = v1[0], v1[1], v2[0], v2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#return the neighbor of v1 with the lowest distance to v2
def lowestDistNeighbor(v1, v2):
    row = v1[0]
    col = v1[1]
    neighbors = [(row-1,col-1),
                 (row-1, col),
                 (row-1,col+1),
                 (row,col-1),
                 (row,col+1),
                 (row+1,col-1),
                 (row+1,col),
                 (row+1,col+1)]
    valid_neighbors = []
    for n in neighbors:
        #make sure our original vertex was not on an edge or corner
        if not(n[0] < 0 or n[0] > len(M) or n[1] < 0 or n[1] > len(M[0])):
            valid_neighbors.append(n)
    
    min_distance = math.inf
    min_dist_v = ()
    for vn in valid_neighbors:
        dist = d(vn, v2)
        if dist < min_distance:
            min_distance = dist
            min_dist_v = vn
    
    return min_dist_v

#returns a boolean representing if v2 is reachable from
# v1 by a straight line path through the occupancy grid
def reachabiliyCheck(v1, v2):
    curr = v1 
    while curr != v2:
        next = lowestDistNeighbor(curr, v2)
        nextRow = next[0]
        nextCol = next[1]  
        if not M[nextRow][nextCol]:
            return False
        curr = next
    return True

def AddVertex(G, vNew, dMax, k):
    G.add_node(k, pos=vNew)
    for vNum in G.nodes:
        v = G.nodes[vNum]['pos']
        dist = d(v, vNew)
        if v != vNew and dist <= dMax and reachabiliyCheck(v, vNew):
            G.add_edge(vNum, k, weight=dist)
            


#return a probabalistic road map corresponding to the occupancy grid M,
#number of desired samples N, and a maximum search radius dMax
def ConstructPRM(N, dMax):
    G = nx.Graph()
    for k in range(N):
        print(k)
        v = sampleVertex()
        AddVertex(G, v, dMax, k)
    return G

# Read image from disk using PIL
occupancy_map_img = Image.open('occupancy_map.png')

# Interpret this image as a numpy array, and threshold its values to → {0,1}
M = (np.asarray(occupancy_map_img) > 0).astype(int)

''' How the graph functions work
# Create empty graph
G = nx.Graph()
# Add vertex v1 at position (r1, c1)
G.add_node(1, pos=(0,0))
# Add vertex v2 at position (r2, c2)
G.add_node(2, pos=(2,2))
# Add an edge between v1 and v2 with weight w12
G.add_edge(1, 2, weight=10)
print(G.nodes[1])
'''

G = ConstructPRM(100, 75)
posDict = {}
for vNum in G.nodes:
    posDict[vNum] = G.nodes[vNum]['pos']
plt.imshow(occupancy_map_img)
nx.draw_networkx(G, posDict, node_size=5, with_labels=False)
plt.show()