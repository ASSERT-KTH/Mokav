def func(*args):
	ret_values = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	if (b > 0):
	    Sum = (a + (b % n))
	    if (Sum > n):
	        Sum = (Sum - n)
	    ret_values.append(Sum)
	elif (b < 0):
	    Sum = (a - (abs(b) % n))
	    if (Sum <= 0):
	        Sum = (Sum + n)
	    ret_values.append(Sum)
	elif (b == 0):
	    ret_values.append(a)

	return ret_values
