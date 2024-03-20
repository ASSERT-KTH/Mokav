def func(*args):
	
	(*m, d) = (int(args[0]) for i in range(5))
	return(sum(((1 - all((((i + 1) % k) for k in m))) for i in range(d))))
