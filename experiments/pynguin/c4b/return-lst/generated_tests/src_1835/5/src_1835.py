def func(*args):
	ret_values = []
	
	x = args[0]
	x = str.split(x, ' ')
	n = int(x[0])
	m = int(x[1])
	if ((n % m) is 0):
	    ret_values.append((n + m))
	else:
	    p = (n // m)
	    while True:
	        temp = (p * m)
	        if (temp > n):
	            ret_values.append(temp)
	            break
	        p += 1

	return ret_values
