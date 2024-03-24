def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split(' '))
	for i in range(0, 10001):
	    if ((((c - (a * i)) % b) == 0) and ((c - (a * i)) >= 0)):
	        ret_values.append('Yes')
	        break
	else:
	    ret_values.append('No')

	return ret_values
