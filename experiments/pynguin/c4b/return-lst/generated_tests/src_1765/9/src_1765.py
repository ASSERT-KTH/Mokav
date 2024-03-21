def func(*args):
	ret_values = []
	
	powers = [1, 2, 4]
	for i in range(3, 50):
	    if (i == 13):
	        powers.append(8092)
	    else:
	        powers.append((2 * powers[(i - 1)]))
	ret_values.append(powers[int(args[0])])

	return ret_values
