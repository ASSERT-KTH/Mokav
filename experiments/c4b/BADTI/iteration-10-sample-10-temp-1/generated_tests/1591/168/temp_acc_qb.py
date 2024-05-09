def patched_func(*args):
	global_list = []
	
	from math import ceil
	i = int(args[0])
	if (i == 3):
	    k = 5
	else:
	    k = ceil((((2 * i) - 1) ** 0.5))
	    if ((k % 2) == 0):
	        k += 1
	for j in range(k, 101):
	    if ((((j ** 2) + 1) / 2) >= i):
	        global_list.append(j)
	        break
	return global_list