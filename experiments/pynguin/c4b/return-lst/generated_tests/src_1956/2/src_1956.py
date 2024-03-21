def func(*args):
	ret_values = []
	
	n = int(args[0])
	row = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	if (n <= 5):
	    ret_values.append(row[(n - 1)])
	else:
	    while (n > 5):
	        n = ((n - 5) / 2)
	    ret_values.append(row[int(n)])

	return ret_values
