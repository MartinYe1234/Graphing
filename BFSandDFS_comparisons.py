# Import and shorten names
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
from random import choice
from time import time

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


#Generate random graph with 200 nodes
def gen_graph():	
	global adj, adjacent
	adj = {}
	adjacent = {}
        #create adjacency lists
	for i in range(num_of_nodes):
		adj[i] = []
		adjacent[i] = []
	#generate random pairs of cities to connect. Beware of double-edges.
	for i in range(num_of_connections):
		#x and y are both random cities that will be connected by a road
		x = randint(0,num_of_nodes-1)
		y = randint(0,num_of_nodes-1)
		#City x is a neighbor to city y and vice versa
		adj[x].append(y)
		adj[y].append(x)
		adjacent[x].append(y)
		adjacent[y].append(x)
	#Delete all duplicates in lists using sets.
	for i in range(num_of_nodes):
		adj[i] = list(set(adj[i]) - set([i]))
		adjacent[i] = list(set(adjacent[i]) - set([i]))


def dfs(node):
        #Mark node as visited, visit all not visited neighbors
	dfs_visited[node] = 1
	for neighbor in adj[node]:
		if not dfs_visited[neighbor]:
			dfs(neighbor)


def bfs(node):
	#add vertex to queue
        queue.append(node)
	#mark as visited
        bfs_visited[node] = 1
        #while there is something in the queue
        while queue:
	#for each adjacent node to the current node
                for neighbour in adjacent[queue[0]]:
	                #if the vertex has not been visited yet
                        if bfs_visited[neighbour] == 0:
                                #add adjacent (neighbour) node to queue
                                queue.append(neighbour)
                                #mark as visited
                                bfs_visited[neighbour] = 1
                queue.pop(0)


#bfs/dfs will be run multiple times on the same graph, the average will be graphed
dfs_runtime = 0.0
bfs_runtime = 0.0
runs = 200

#200 Nodes per graph and number of connections increase
for num_of_connections in range(0,2001):
        num_of_nodes = 200
	#Adjacency array is a python dictionary
	#adj[i] has all neighbors of vertex i
        adj = {}
        adjacent = {}
        #how many times to generate and run dfs/bfs on randomly generated graphs, 200
        for i in range(runs):
                #generate graph
                gen_graph()
                #dfs in blue
                dfs_visited = [0 for i in range(num_of_nodes)]
                queue = []
                #start timing runtime
                dfs_time = time()
                dfs(0)
                #add to runtime
                dfs_runtime += (time() - dfs_time)
                #bfs in orange
                bfs_visited = [0 for i in range(num_of_nodes)]
                queue = []
                bfs_time = time()
                bfs(0)
                #add to runtime
                bfs_runtime += (time() - bfs_time)         
        #send the average of the runtimes to graph, rounded to 13 decimal places
        dfs_data.append(round((dfs_runtime/runs),13))
        bfs_data.append(round((bfs_runtime/runs),13))
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
