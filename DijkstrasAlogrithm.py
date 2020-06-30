'''
Algorithm to find out the shortest path from node 'A' to node 'B' in a connected graph
Links are considered to be bi-directional. 

Graph is stored as a dictionary. The keys are the names of the nodes. Values are the list of links at each node. 
E.g, A simple graph with nodes A,B,C and weight of the links A to B is 5, A to C is 2 and B to C is 1
will be stored as below. 

graph = {
	'A':[['B',5],['C',2]],
	'B':[['A',5],['C',1]],
	'C':[['B',1],['A',2]]
} 
'''

def is_node_in_graph(node,graph):
	'''
	returns True if the node is present in the graph
	'''
	return node in graph.keys()

def add_link_to_graph(link,graph):
	'''
	Adds the link to the graph and returns the graph. 
	link should be a tuple (start_node,end_node,weight)
	'''
	(a,b,wt) = link 
	if is_node_in_graph(a,graph): 
		if b not in [link[0] for link in graph[a]]:
			graph[a].append([b,wt])
	else:
		graph[a] = [[b,wt]]

	# If you want to make the graph uni-directional comment the next if else condition. 
	# You might also need to consider adding an empty end_node to the graph if required.

	if is_node_in_graph(b,graph): 
		if a not in [link[0] for link in graph[b]]:
			graph[b].append([a,wt])
	else:
		graph[b] = [[a,wt]]

	return(graph)

def get_link():
	'''
	This will get links from the user. 
	'''
	while True:
		link = input('Enter the link with weight in x,y,0 format : ')
		nodes = link.split(',')
		if len(nodes) < 3:
			print('Enter both from and to nodes along with weight using a comma separator')
			continue
		elif len(nodes) > 3: 
			print('More than 2 nodes entered. Ignoring the rest')
		try: 
			return((nodes[0],nodes[1],float(nodes[2])))
		except ValueError: 
			print('Weight is not a number. Try again')

def find_shortest_path(start_node,end_node,graph): 
	'''
	Find the shortest path from start node to end node in the graph. 
	'''
	node_fields = {}
	short_path = [end_node]

	#Create a dictionary of fields for each node. The key will be node name. The value will be a list. 
	#The list contains the [distance (from start node),predecessor_node,Boolean(to check if neode is traversed)]
	
	for node in graph.keys(): 
		node_fields[node] = [9999999,'',False]
		if node == start_node: 
			node_fields[node][0] = 0

	#In the above for loop node fields are defined and for start node initiated with default values

	work_node = start_node
	#startin  with the first node, we will parse through all the nodes to find the shortest path. 

	while True: 
		
		for link in graph[work_node]:
			#For all the links to the node, check the shortest distance and update it if a new path is found. 
			if node_fields[link[0]][0] > link[1] + node_fields[work_node[0]][0] and node_fields[link[0]][2] == False:
				node_fields[link[0]][0] = link[1] + node_fields[work_node[0]][0]
				node_fields[link[0]][1] = work_node

		# All the nodes linked to your work node has been updated. Now find the next nearest node to work with it. 

		node_fields[work_node][2] = True
		lengths = [(key,value[0]) for (key,value) in node_fields.items() if value[2] == False]

		# lengths is a tuple (node,distance) for all the not traversed nodes. 

		short_length = 9999999
		work_node = ' '
		if len(lengths) == 0:
			# No more nodes to traverse. Break from the loop. 
			break
		else:
			# Find the next nearest node 
			for length in lengths:
				if short_length > length[1]:
					work_node = length[0]

		# If the next nearest node is end node, we can stop or if there are no nodes (disconnected graphs)
		if work_node == end_node or work_node == ' ': 
			break

	work_node = end_node
	# Traverse through the node fields and get the path. Second field will tell us the previous node. 

	while True:
		if node_fields[work_node][1] == '': 
			print(f'There is no connection between {start_node} and {end_node}')
			break
		elif node_fields[work_node][1] == start_node: 
			short_path.append(node_fields[work_node][1])
			print('Shortest Path is : ')
			print(' --> '.join(short_path[::-1]))
			print(f'Final distance is : {node_fields[end_node][0]}')
			break
		else:
			short_path.append(node_fields[work_node][1])
			work_node = node_fields[work_node][1]


def main(): 
	'''
	Main logic to control the user input and print output. 
	'''
	links_list = []
	graph = {}

	# Get the links from the user. 

	while True: 
		links_list.append(get_link())
		cont = input('Do you have more links Y/N : ')
		if cont.lower()[0] == 'n':
			break

	# Print the links for reference and create a graph simulatneously.
	print('List of links is : ')

	for link in links_list:
		print(link)
		graph = add_link_to_graph(link,graph)

	# Print the final graph created for reference

	print('\nGraph of the above links is: ')
	print(graph)

	while True: 
		start_node = input('Enter the start node : ')
		if is_node_in_graph(start_node,graph):
			break
		else:
			print('Node is not present in the graph. Try again')

	while True: 
		end_node = input('Enter the end node : ')
		if is_node_in_graph(end_node,graph):
			break
		else:
			print('Node is not present in the graph. Try again')

	find_shortest_path(start_node,end_node,graph)

if __name__ == '__main__':
	main()

