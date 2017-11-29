# FA10 2

# Find a way to sort where at any point the node is connected. 

def DFS-connected(G):
	"""
	Initialize unexplored nodes and search each node.
	"""

	for each U \belonging_to G.v:
		u.color = white # Unexplored
		u.parent = NIL # \pi

	t = 0 

	global largest = -inf #
	global second_largest = -inf #
	global depth_counter = 0 #

	source = G.v[0] # So we don't jump to just any node (potentially an unconnected node), after a run of DFS-visit, we establish a source to become an anchor/reference point of sorts. 

	for each u \belonging_to G.adj[root]: # Instead of iterating through vertices by number, we immediately start with the process of analyzing all nodes adjacent to the source. By the nature of an undirected connected graph, which is given, the search will still cover the whole graph. Except now, it's ensured that each subgraph is connected.
		if u.color == white:
			DFS-visit(G,u)

	return largest + second_largest # The diameter (greatest depth)

def DFS-visit-connected(G,u):
	
	t = t+1 # Progress time.  
	u.d = t # Discovery time of u is current time. 
	u.color = gray # Being explored. 
	
	depth_counter += 1 #

	for each v \belonging_to G.adj[u]: # adjacent to u
		if v.color == white:
			v.parent = u
			DFS-visit(G, v)

	u.color = black # Explored. 
	t=t+1 # Progress time. 
	u.f = t # Finish time of u is current time. 