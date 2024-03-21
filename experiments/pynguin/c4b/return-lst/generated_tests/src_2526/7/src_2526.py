def func(*args):
	ret_values = []
	
	n = args[0]
	n = int(n)
	if (n <= 2):
	    ret_values.append((- 1))
	elif (n <= 50):
	    result = [i for i in range(n, 0, (- 1))]
	    for el in result:
	        ret_values.append(el, end=' ')
	else:
	    ret_values.append((- 1))

	return ret_values
