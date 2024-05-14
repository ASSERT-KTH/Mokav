def original_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = list(map(int, args[0].split()))
	aux = v0
	i = 1
	while (c > aux):
	    aux += min((v0 + (i * a)), v1)
	    i += 1
	global_list.append(i)
	return global_list