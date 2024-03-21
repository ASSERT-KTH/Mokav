def func(*args):
	ret_values = []
	
	s = args[0].split()
	a = int(s[0])
	b = int(s[1])
	n = int(s[2])
	if (n == 0):
	    ret_values.append(b)
	elif (b > 0):
	    if (((n + b) % a) == 0):
	        ret_values.append(a)
	    else:
	        ret_values.append(((n + b) % a))
	elif (b < 0):
	    ret_values.append((abs((a - b)) % n))

	return ret_values
