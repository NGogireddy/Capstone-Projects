'''
This module will take the links from the user, build a graph and check if it has Eulars path/circuit or not. 
This solution works for undirectional graphs only.
'''

def is_node_in_graph(node,graph):
	'''
	returns True if the node is defined in the graph
	'''
	return node in graph.keys()

def add_link_to_graph(link,graph):
	'''
	Adds the link to the graph and returns the graph. 
	'''
	(a,b) = link 
	if is_node_in_graph(a,graph): 
		graph[a].append(b)
	else:
		graph[a] = list(b)

	if is_node_in_graph(b,graph): 
		graph[b].append(a)
	else:
		graph[b] = list(a)

	return(graph)

def get_link():
	'''
	This will get links from the user. 
	'''
	while True:
		link = input('Enter the link in x,y format : ')
		nodes = link.split(',')
		if len(nodes) < 2:
			print('Enter both from and to nodes with a comma separator')
			continue
		elif len(nodes) > 2: 
			print('More than 2 nodes entered. Ignoring the rest')
		return((nodes[0],nodes[1]))

def is_connected(graph): 
	'''
	Returns True if the graph is connected
	'''
	nodes_list = list(graph.keys())
	node = nodes_list[0]
	connected_nodes = list(node)

	# We are picking a random node and try to find all the connected nodes. 
	for node in connected_nodes: 
		# For each node loop through the connected nodes
		for nodes in graph[node]: 
			# If the node is already added in the connected nodes dont add it again. 
			if nodes not in connected_nodes:
				connected_nodes.append(nodes)

	# For a picked node all connected nodes are found. Compare the count with total nodes. 
	# Connected graph will return true
	return(len(connected_nodes) == len(nodes_list))


def get_degrees(graph): 
	'''
	Calculate the degree of each node and return it as a list of tuples. 
	'''
	degree_list = []
	for node in graph.keys(): 
		degree_list.append((node,len(graph[node])))

	return degree_list

def possible_euler_path(degree_list):
	'''
	Returns True if euler path is possible. 
	'''
	odd_degree_count = 0
	for node,degree in degree_list: 
		if degree%2 == 1: 
			odd_degree_count += 1
	return(odd_degree_count == 0 or odd_degree_count == 2)

def get_start_node(degree_list):
	'''
	Returns the starting node. If there is a node with odd degree return the node with least odd degree
	'''
	count = 0
	for node,degree in degree_list:
		if degree%2 == 1:
			if count == 0: 
				count+= 1
				node1,degree1 = node,degree
			else:
				return(node if degree < degree1 else node1)
			
	return node

def get_euler_path(start_node,graph): 
	'''
	Get the next link in Euler path. Recursively call the function to get path.  
	'''
	next_node = graph[start_node][0]
	path = next_node + ' --> '
	graph[start_node].remove(next_node)
	graph[next_node].remove(start_node)
	if len(graph[next_node]) != 0: 
		return(path + get_euler_path(next_node,graph))
	else:
		return(next_node)

def main(): 
	'''
	Main logic to control the user input and print output. 
	'''
	links_list = []
	graph = {}
	eulers_path = ''

	# Get the links of the graph from the user. 
	while True: 
		links_list.append(get_link())
		cont = input('Do you have more links Y/N : ')
		if cont.lower()[0] == 'n':
			break

	print('\nList of links is : ')

	# Print the links and create a graph from it. 

	for link in links_list:
		print(link)
		graph = add_link_to_graph(link,graph)

	print('\nGraph of the above links is: ')
	print(graph)

	# Check if the graph is connected and find the Euler's path/circuit.

	if is_connected(graph): 
		print('\nGraph is connected')
		degree_list = get_degrees(graph)

		if possible_euler_path(degree_list): 
			start_node = get_start_node(degree_list)
			if len(graph[start_node])%2 == 1: 
				print('Eulers circuit is not possible, however path can be present')
			else: 
				print('Eulers circuit for the graph is : ')
			eulers_path = start_node + ' --> ' + get_euler_path(start_node,graph)
			print(eulers_path)
		else:
			print('Euler path is not possible as there are one or more than 2 node(s) with odd degree')
	else:
		print('Graph is not connected. Euler path/circuit is not possible')

	
if __name__ == '__main__':
	main()

