def func(*args):
	ret_values = []
	
	s_1 = args[0]
	l_1 = s_1.split()
	c = int(l_1[0])
	v = int(l_1[1])
	v1 = int(l_1[2])
	a = int(l_1[3])
	l = int(l_1[4])
	x = v
	i = 1
	while (x < c):
	    if ((v + a) < v1):
	        v += a
	    else:
	        v = v1
	    x = ((x + v) - l)
	    i += 1
	ret_values.append(i)

	return ret_values
