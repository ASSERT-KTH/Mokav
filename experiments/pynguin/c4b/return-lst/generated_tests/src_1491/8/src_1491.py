def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range((n + 1), 10000):
	    if (len({int(j) for j in ' '.join(str(i)).split()}) == 4):
	        ret_values.append(i)
	        break

	return ret_values
