def func(*args):
	ret_values = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	s = v0
	i = 1
	while (c > s):
	    s += min((v0 + (i * a)), v1)
	    i += 1
	    s -= l
	ret_values.append(i)

	return ret_values
