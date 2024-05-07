def original_func(*args):
	global_list = []
	
	from math import ceil
	i = int(args[0])
	k = ceil((((2 * i) - 1) ** 0.5))
	for j in range(k):
	    if ((((j ** 2) + 1) / 2) >= i):
	        global_list.append(j)
	        break
	return global_list