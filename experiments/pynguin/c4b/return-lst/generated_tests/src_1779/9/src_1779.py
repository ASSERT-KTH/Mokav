def func(*args):
	ret_values = []
	
	m = args[0].split(' ')
	n = int(m[0])
	a = int(m[1])
	b = int(m[2])
	k = ((a + b) % n)
	if (k == 0):
	    k = n
	ret_values.append(k)

	return ret_values
