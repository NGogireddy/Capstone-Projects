'''
Program to find out the Minimum spanning Tree in a connected graph
Links are considered to be bi-directional. 

Graph is stored as a dictionary. The keys are the names of the nodes. Values are the list of links at each node. 
E.g, A simple graph with nodes A,B,C and weight of the links A to B is 5, A to C is 2 and B to C is 1
will be stored as below. 

graph = {
	'A':[['B',5],['C',2]],
	'B':[['A',5],['C',1]],
	'C':[['B',1],['A',2]]
} 

Minimum spanning tree for the above graph would be 

('A','C',2), ('B','C',1)

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

def find_minimum_spanning_tree(graph): 
	'''
	Find the tree covering all the nodes with least weight. 
	'''
	min_tree_set = set()
	node_set = set(graph.keys())
	min_spanning_tree = []

	# pick a random node
	work_node = node_set.pop()
	print(work_node)

	min_tree_set.add(work_node)
	print(min_tree_set)
	print(node_set)

	while len(node_set): 

		#Loop through all the nodes in min_tree_set and find the nearest node.
		short_length = 999999

		for work_node in min_tree_set:
			# find the nearest node to the work node 
			print(f'\nWorking with work_node {work_node}')
			for link in graph[work_node]:
				print(f'Working with link {link}')
				if short_length > link[1] and link[0] not in min_tree_set:
					short_length = link[1]
					near_node = link[0]
					start_node = work_node

		# Nearest node is present in near_node and short_length has got the weight
		# Add the link to the minimum spanning tree
		min_spanning_tree.append((start_node,near_node,short_length))
		print(f'{start_node} , {near_node} and {short_length} is in min span tree')

		# Remove the node from node_set and add it to the min_tree_set
		print(f'Node set is : {node_set}')
		print(f'Tree set is : {min_tree_set}')
		node_set.remove(near_node)
		min_tree_set.add(near_node)
		print(f'Node set is : {node_set}')
		print(f'Tree set is : {min_tree_set}')

	print('Links in the minimum spanning tree are : ')
	print(min_spanning_tree)





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

	find_minimum_spanning_tree(graph)

if __name__ == '__main__':
	main()

