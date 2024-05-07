def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	totale = (4 * 60)
	cont = 0
	i = 0
	totale -= k
	while True:
	    i += 1
	    if (((totale - (i * 5)) >= 0) and (n > 0)):
	        n -= 1
	        totale = (totale - (i * 5))
	        cont += 1
	    else:
	        break
	global_list.append(cont)
	return global_list