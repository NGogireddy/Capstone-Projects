'''
This module will take the links from the user, build a graph and check if it has Eulars path/circuit or not.
This solution is for directional graph 
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

	if not is_node_in_graph(b,graph): 
		graph[b] = list()

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

def get_degrees(graph): 
	'''
	Calculate the in-degree and out-degree of each node and return it as a dictionary. 
	Returns a dictionary with degree's for each node. 
	Key is the node name. Value is a list [outdegree, indegree, outdegree-indegree]
	'''
	degree = {}
	for node in graph.keys(): 
		degree[node] = [len(graph[node]),0,0]
	for node in graph.keys():
		for out_node in graph[node]: 
			degree[out_node][1] += 1
	for node in graph.keys(): 
		degree[node][2] = degree[node][0] - degree[node][1]

	return degree

def verify_in_out_degree(degree,graph):
	'''
	Checks the out-degree - in-degree and see i
	Return '0' for No Euler path or Euler circuit
	Return node name if Euler path or Euler circuit is possible
	'''
	start_count = 0
	end_count = 0
	return_node = ''
	end_node = ''
	for node in graph.keys(): 
		if degree[node][2] > 1 or degree[node][2] < -1: 
			return('0')
		if degree[node][2] == 1: 
			start_count += 1
			return_node = node
		if degree[node][2] == -1: 
			end_count += 1
			end_node = node
	if start_count > 1 or end_count > 1:
		return('0')
	if start_count == 0 and end_count == 0:
		return(node)
	return(return_node)

def get_euler_path(start_node,graph,degrees): 
	'''
	Get the next link in Euler path and recursively call this function to get the path/circuit.  
	'''
	next_node = ''
	count = 0

	# The next node is the one which has most outdegree in its directly linked nodes.  
	
	for node in graph[start_node]: 
		if count < degrees[node][0]:
			count = degrees[node][0]
			next_node = node
	if next_node == '':
		next_node = graph[start_node][0]

	# Remove the link and attach it to the Eulers path/circuit. 

	degrees[start_node][0] -= 1
	degrees[next_node][1] -= 1
	path = next_node + ' --> '
	graph[start_node].remove(next_node)

	if len(graph[next_node]) != 0: 
		return(path + get_euler_path(next_node,graph,degrees))
	else:
		return(next_node)

def main(): 
	'''
	Main logic to control the user input and print output. 
	'''
	links_list = []
	graph = {}
	eulers_path = ''

	# Gets the links from the user. 
	while True: 
		links_list.append(get_link())
		cont = input('Do you have more links Y/N : ')
		if cont.lower()[0] == 'n':
			break

	# Prints the links and create a graph. 

	print('\nList of links is : ')
	for link in links_list:
		print(link)
		graph = add_link_to_graph(link,graph)

	print('\nGraph of the above links is: ')
	print(graph)

	degrees = get_degrees(graph)
	degree_check = verify_in_out_degree(degrees,graph)

	if degree_check == '0':
		print('\nEuler path or circuit is not possible')
	else: 
		eulers_path = degree_check + ' --> ' + get_euler_path(degree_check,graph,degrees)
		if eulers_path[0] == eulers_path[-1]:
			print('\nEulers circuit is : ')
		else:
			print('\nEulers path is :')
		print(eulers_path)
	
if __name__ == '__main__':
	main()

