def original_func(*args):
	global_list = []
	
	s = args[0]
	n = int(s[0])
	k = int(s[2])
	secuencia = '1'
	i = 1
	while (i < n):
	    nueva_secuencia = ((secuencia[:] + str((i + 1))) + secuencia[:])
	    secuencia = nueva_secuencia
	    i += 1
	global_list.append(secuencia[(k - 1)])
	return global_list