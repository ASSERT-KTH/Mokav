def func(*args):
	ret_values = []
	
	(n, a, b, c) = args[0].split()
	n = int(n)
	resto = (4 - (n % 4))
	if (resto == 4):
	    ret_values.append(0)
	elif (resto == 1):
	    ret_values.append(min([int(a), (int(b) + int(c)), (int(c) * 3)]))
	elif (resto == 2):
	    ret_values.append(min([(int(a) * 2), int(b), (int(c) * 2)]))
	else:
	    ret_values.append(str(min([(int(a) * 3), (int(a) + int(b)), int(c)])))

	return ret_values
