def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = 'aabb'
	s = ''
	for i in range(n):
	    s += a[(i % 4)]
	ret_values.append(s)

	return ret_values
