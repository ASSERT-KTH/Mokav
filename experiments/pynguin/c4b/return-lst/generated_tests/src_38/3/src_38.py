def func(*args):
	ret_values = []
	
	n = (int(args[0]) - 1)
	while (n > 4):
	    n = ((n - 5) // 2)
	ret_values.append(['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][n])

	return ret_values
