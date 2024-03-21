def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range((n + 1), 10000):
	    if (len(set(str(i))) == len(str(i))):
	        ret_values.append(i)
	        break

	return ret_values
