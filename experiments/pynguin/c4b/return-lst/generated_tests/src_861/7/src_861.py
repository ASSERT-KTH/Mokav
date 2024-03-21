def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split(' '))
	if (a < b < c):
	    k = ((c - b) + (b - a))
	    ret_values.append(k)
	elif (b < a < c):
	    k = ((c - a) + (a - b))
	    ret_values.append(k)
	elif (a < c < b):
	    k = ((b - c) + (c - a))
	    ret_values.append(k)
	elif (c < b < a):
	    k = ((a - b) + (b - c))
	    ret_values.append(k)
	elif (c < a < b):
	    k = ((b - a) + (a - c))
	    ret_values.append(k)
	elif (b < c < a):
	    k = ((a - c) + (c - b))
	    ret_values.append(k)

	return ret_values
