def original_func(*args):
	global_list = []
	
	n = int(args[0])
	L = args[1]
	cont = 0
	k = 0
	while (k < (n - 1)):
	    if (L[k] != L[(k + 1)]):
	        break
	    else:
	        cont += 1
	    k += 1
	global_list.append(cont)
	return global_list