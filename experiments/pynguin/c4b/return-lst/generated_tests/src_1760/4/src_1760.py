def func(*args):
	ret_values = []
	
	s = oct(int(args[0]))
	counter = 0
	for c in s:
	    if (c == '1'):
	        counter += 1
	ret_values.append(counter)

	return ret_values
