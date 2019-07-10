# Import and shorten names
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
from random import choice
from time import time
from sys import setrecursionlimit
setrecursionlimit(25000)

# Create rectangle
fig = plt.figure()
#DFS data to plot
dfs_data = []
#BFS
bfs_data = []
#generates x axis to plot the data on
x_axis = [i+1 for i in range(2001)]
#formatting of graphs
plt.figure(figsize=(16, 5))
#finds all possible cities reachable from a certain vertex
def dfs(vertex):
#Mark as visited, visit all not visited neighbors
	dfs_visited[vertex] = 1
	for neighbor in adj[vertex]:
		if not dfs_visited[neighbor]:
			dfs(neighbor)
#runs bfs
def bfs(vertex):
    queue.append(vertex)
    bfs_visited[vertex] = 1
    while queue:
        cur = queue.pop(0)
        bfs_visited[cur] = 1
        for neighbour in adjacent[cur]:
            if not bfs_visited[neighbour]:
                queue.append(neighbour)
#Generate random graph
def regen_graph():	
	global adj, adjacent
	adj = {}
	adjacent = {}
	for i in range(N):
		#create an array for each vertex that contains all vertexes adjacent to it
		adj[i] = []
		adjacent[i] = []
	#generate M random pairs of cities to connect. Beware of double-edges.
	for i in range(M):
		#x and y are both random cities that will be connected by a road
		x = randint(0,N-1)
		y = randint(0,N-1)
		#City x is a neighbor to city y and vice versa
		adj[x].append(y)
		adj[y].append(x)
		adjacent[x].append(y)
		adjacent[y].append(x)
	#Delete all duplicates in lists using sets.
	for i in range(N):
		adj[i] = list(set(adj[i]) - set([i]))
		adjacent[i] = list(set(adjacent[i]) - set([i]))
#bfs/dfs will be run multiple times on the same graph, the average will be graphed
dfs_runtime = 0.0
bfs_runtime = 0.0
runs = 2
#200 Nodes per graph and number of connections increase
for M in range(0,2001):
	#N is the number of citites
        N = 200
	#Adjacency array is a python dictionary
	#adj[i] has all neighbors of vertex i
        adj = {}
        adjacent = {}
        #how many times to generate and run dfs/bfs on randomly generated graphs
        for i in range(runs):
                #generate a random graph with M connections and N nodes
                regen_graph()
                #dfs in blue
                dfs_visited = [0 for i in range(N)]
                queue = []
                #start timing runtime
                dfs_time = time()
                dfs(0)
                #add to runtime
                dfs_runtime += (time() - dfs_time)
                #bfs in orange
                bfs_visited = [0 for i in range(N)]
                queue = []
                bfs_time = time()
                bfs(0)
                #add to runtime
                bfs_runtime += (time() - bfs_time)
        #send the average of the runtimes to graph, rounded to 7 decimal places
        dfs_data.append(round((dfs_runtime/runs),7))
        bfs_data.append(round((bfs_runtime/runs),7))
        #reset runtime for next round
        dfs_runtime = 0.0
        bfs_runtime = 0.0
#label along x axis
plt.xlabel("# of connections between nodes")
#label along y axis
plt.ylabel("Runtime (seconds)")
#title of graph
plt.title("BFS(Orange)/DFS(Blue) comparison")
#plotting data
plt.plot(x_axis,dfs_data)
plt.plot(x_axis,bfs_data)
plt.show()
