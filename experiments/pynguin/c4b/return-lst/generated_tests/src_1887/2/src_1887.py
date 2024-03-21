def func(*args):
	ret_values = []
	
	(a, b) = args[0].split(' ')
	(a, b) = (int(a), int(b))
	c = (a - b)
	if (((a % c) == 0) and ((b % c) == 0)):
	    ret_values.append('Equal')
	elif (a > b):
	    ret_values.append('Masha')
	else:
	    ret_values.append('Dasha')

	return ret_values
