'''
This module will take the links from the user, build a graph and check if it is connected or not. 
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
		if b not in graph[a]:
			graph[a].append(b)
	else:
		graph[a] = list(b)

	if is_node_in_graph(b,graph): 
		if a not in graph[b]:
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

def main(): 
	'''
	Main logic to control the user input and print output. 
	'''
	links_list = []
	graph = {}

	while True: 
		links_list.append(get_link())
		cont = input('Do you have more links Y/N : ')
		if cont.lower()[0] == 'n':
			break

	print('List of links is : ')

	for link in links_list:
		print(link)
		graph = add_link_to_graph(link,graph)

	print('\nGraph of the above links is: ')
	print(graph)

	if is_connected(graph): 
		print('Graph is connected')
	else:
		print('Graph is not connected')

if __name__ == '__main__':
	main()

