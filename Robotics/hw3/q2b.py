import heapdict
import math
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

'''a function that takes as input the start state s, goal state g, and
populated predecessor map pred, and returns the sequence of vertices on the optimal
path from s to g.'''
def RecoverPath(s, g, pred):
    curr = g
    result = []
    while(curr != s):
        result.insert(0, curr)
        curr = pred[curr]
    result.insert(0,s)
    return result

#do an A* search algorithm and return an array representing the list of
#vertices along the optimal path to the goal g from the start s
#return the empty list if there was no optimal path
def A_STAR_SEARCH(V, s, g, N, w, h):
    CostTo = {} #cost (value) to get from the start node s to v (key)
    pred = {} #the previous node (value) from the target node v (key) on the shortest path
    '''is a map that assigns to each vertex v (key) the sum CostTo(v) + h(v,g) (value),
    the sum of the cost of the best known path to v and the predicted cost of the best
    path from v to the goal g; this is the estimated cost of the optimal path from the start
    s to the goal g that passes through vertex v.'''
    EstTotalCost = {} 
    Q = heapdict.heapdict() #a priority queue in which elements with lower values are removed first.
    for v in V:
        CostTo[v] = math.inf
        EstTotalCost[v] = math.inf
    CostTo[s] = 0
    EstTotalCost[s] = h(s,g)
    Q[s] = h(s,g)
    while len(Q) != 0:
        v = Q.popitem()
        v = v[0] #get the vertex without the priority
        if v == g:
            return RecoverPath(s, g, pred)
        for i in N(v):
            pvi = CostTo[v] + w(v,i)
            if pvi < CostTo[i]:
                pred[i] = v
                CostTo[i] = pvi
                EstTotalCost[i] = pvi + h(i,g)
                Q[i] = EstTotalCost[i]
    return []

# Read image from disk using PIL
occupancy_map_img = Image.open('occupancy_map.png')

# Interpret this image as a numpy array, and threshold its values to → {0,1}
M = (np.asarray(occupancy_map_img) > 0).astype(int)

def N(v):
    row = v[0]
    col = v[1]
    neighbors = [(row-1,col-1),
                 (row-1, col),
                 (row-1,col+1),
                 (row,col-1),
                 (row,col+1),
                 (row+1,col-1),
                 (row+1,col),
                 (row+1,col+1)]
    unoccupied_neighbors = []
    for n in neighbors:
        #make sure our original vertex was not on an edge or corner
        if n[0] < 0 or n[0] >= len(M) or n[1] < 0 or n[1] >= len(M[0]):
            continue
        #only add unoccupied neighbors
        if M[n[0]][n[1]]:
            unoccupied_neighbors.append(n)
    return unoccupied_neighbors

#euclidean distance between two vectors v1 and v2
def d(v1, v2):
    x1, y1, x2, y2 = v1[0], v1[1], v2[0], v2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def totalPathLength(pathArr):
    totalLen = 0
    for i in range(len(pathArr)-1):
        totalLen += d(pathArr[i], pathArr[i+1])
    return totalLen

#get the vertex set V from the occupancy grid
V = set()
for i in range(len(M)):
    for j in range(len(M[0])):
        V.add((i,j))

opt_path = A_STAR_SEARCH(V, (635,140), (350,400), N, d, d)
print(totalPathLength(opt_path))
xs, ys = [], []
for i in opt_path:
    xs.append(i[1])
    ys.append(i[0])
plt.plot(xs, ys)
plt.imshow(occupancy_map_img)
plt.show()