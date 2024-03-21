def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = n
	x = 0
	mm = (n % 5)
	if (mm == 0):
	    x = (m // 5)
	    ret_values.append(x)
	elif (m > 5):
	    x = (m // 5)
	    ret_values.append((x + 1))
	elif (n <= 5):
	    ret_values.append('1')

	return ret_values
