'''
Find the closest pair in a give set of co-ordinates using OOPS concepts. 
'''

class Point(): 
	'''
	This is a point class having x,y as attributes and distance method.
	'''

	def __init__(self,x=0,y=0): 
		self.x = x
		self.y = y

	def __str__(self):
		return f"({self.x},{self.y})"

	def distance(self,point2):
		'''
		Returns the distance between self and point2.
		'''

		return(((point2.x-self.x)**2+(point2.y-self.y)**2)**0.5)

def get_closest_points(points_list): 
	'''
	Returns a tuple of closest points
	'''
	closest_distance = 999999999
	total_points = len(points_list)
	first_index = 0

	for point1 in points_list:
		first_index += 1
		second_index = first_index
		while second_index < total_points: 
			distance = point1.distance(points_list[second_index])
			if distance < closest_distance: 
				answer1 = point1
				answer2 = points_list[second_index]
				closest_distance = distance
			second_index += 1

	return(answer1,answer2)


def get_point(): 
	'''
	This will get co-ordinates from the user, validate it and creates a point object. 
	'''
	while True:
		point = input('Enter the co-ordinates in x,y format : ')
		coordinates = point.split(',')
		if len(coordinates) < 2:
			print('Enter both x and y co-ordinates with a comma separator')
			continue
		elif len(coordinates) > 2: 
			print('More than 2 co-ordinates entered. Ignoring the rest')
		try: 
			return(Point(float(coordinates[0]),float(coordinates[1])))
		except:
			print('Enter only floating point values for coordinates. Try again')
		else:
			break

def main(): 
	'''
	Main logic to control the user input and print output. 
	'''
	points_list = []

	while True: 
		points_list.append(get_point())
		cont = input('Do you have more points Y/N : ')
		if cont.lower()[0] == 'n':
			break

	print('List of points is : ')

	for point in points_list:
		print(point)

	point1,point2 = get_closest_points(points_list)
	print('\nClosest pair is : ')
	print(point1)
	print(point2)

if __name__ == '__main__':
	main()