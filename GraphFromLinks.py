'''
This program creates a graph from the links entered. 

A link is a tuple of start node and end node. 
e.g, (a,b) means a link between a to b.

Graph is a dictionary. 
The keys are the nodes present in the graph and values are the nodes linked to it. 

graph = {a:[b,c], b:[a], c:[a]}

There are only two links in the above graph. a linked to b and also to c. 

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

if __name__ == '__main__':
	main()

