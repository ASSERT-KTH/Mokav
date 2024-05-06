def original_func(*args):
	global_list = []
	
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0])
	(length_of_row, circle) = (5, 0)
	while (n > 0):
	    n -= length_of_row
	    length_of_row *= 2
	    circle += 1
	n += (length_of_row // 2)
	global_list.append(names[(n // (2 ** (circle - 1)))])
	return global_list