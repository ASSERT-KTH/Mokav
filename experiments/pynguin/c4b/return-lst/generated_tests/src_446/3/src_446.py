def func(*args):
	ret_values = []
	
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0])
	(length_of_row, circle) = (5, 0)
	while (n > 0):
	    n -= length_of_row
	    length_of_row *= 2
	    circle += 1
	n += (length_of_row // 2)
	if ((n % (2 ** (circle - 1))) == 0):
	    ret_values.append(names[((n // (2 ** (circle - 1))) - 1)])
	else:
	    ret_values.append(names[(n // (2 ** (circle - 1)))])

	return ret_values
