def original_func(*args):
	global_list = []
	
	s = args[0]
	d = (s + s)
	l = len(s)
	cont = 0
	for i in range(l):
	    if (d[i:(i + l)] != s):
	        cont += 1
	global_list.append((cont + 1))
	return global_list