def func(*args):
	ret_values = []
	
	s = args[0].split()
	n = int(s[0])
	m = int(s[1])
	z = int(s[2])
	k = 0
	for i in range(1, (z + 1)):
	    if (((i % n) == 0) and ((i % m) == 0)):
	        k += 1
	ret_values.append(k)

	return ret_values
