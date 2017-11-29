# FA10 1.2

# Find D of a tree graph. 

def DFS-modified(G):
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

	for each u \belonging_to G.v:
		if u.color == white:
			DFS-visit(G,u)

	return largest + second_largest # The diameter (greatest depth)

def DFS-visit-modified(G,u):
	
	t = t+1 # Progress time.  
	u.d = t # Discovery time of u is current time. 
	u.color = gray # Being explored. 
	
	depth_counter += 1 #

	for each v \belonging_to G.adj[u]: # adjacent to u
		if v.color == white:
			v.parent = u
			DFS-visit(G, v)

	# Once the for loop is over, that means we're at a leaf. 

	if depth_counter >= largest: # The depth of the leaf, if bigger...
		key = largest 
		largest = depth_counter # is the new largest.
		second_largest = key    # second_largest is the previous largest. 
	
	depth_counter -= 1 # We're traveling backwards once we reach a leaf. 

	u.color = black # Explored. 
	t=t+1 # Progress time. 
	u.f = t # Finish time of u is current time. 

