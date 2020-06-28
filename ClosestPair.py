'''
Program to find the closest pair of points on a 2-D plane. 
'''

def distance_btn_two_points(point1,point2): 
	'''
	Find the distance between point1 and point2
	point is a tuple of x and y co-ordinates
	'''
	return(((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)**0.5)

def find_closest_pair(points_list): 
	'''
	Finds the closest pair in the list of points given.
	'''
	closest_distance = 999999999
	total_points = len(points_list)
	first_index = 0

	for point1 in points_list:
		first_index += 1
		second_index = first_index
		while second_index < total_points: 
			distance = distance_btn_two_points(point1,points_list[second_index])
			if distance < closest_distance: 
				answer1 = point1
				answer2 = points_list[second_index]
				closest_distance = distance
			second_index += 1
	print('Closest pair is : ')
	print(answer1,answer2)


def main(): 
	'''
	Main logic to get the co-ordinates of points from user and display the output
	'''
	points_list  = []

	while True: 
		point = input('Enter the co-ordinates in x,y format or quit to stop : ')
		coordinates = point.split(',')
		if point.lower() == 'quit': 
			break
		try:
			point_tuple = (float(coordinates[0]),float(coordinates[1]))
			points_list.append(point_tuple)
			print(coordinates)
			print(point_tuple)
			print(points_list)
		except ValueError:
			print('Invalid entry. To stop entering the co-ordinates type quit. Try Again')
		except IndexError:
			print('Point should have two co-ordinates separated by a comma')
	print('Points entered are : ')
	print(points_list)
	find_closest_pair(points_list)
		

if __name__ == '__main__':
	main()