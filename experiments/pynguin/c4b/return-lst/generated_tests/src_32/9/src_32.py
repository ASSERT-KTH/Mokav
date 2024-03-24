def func(*args):
	ret_values = []
	
	s = args[0]
	d = (s + s)
	l = len(s)
	c = set()
	for i in range(l):
	    aux = d[i:(i + l)]
	    if (aux not in c):
	        c.add(aux)
	ret_values.append(len(c))

	return ret_values
