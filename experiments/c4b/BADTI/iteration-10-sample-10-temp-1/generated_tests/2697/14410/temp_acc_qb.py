def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	for i in range(0, 101):
	    j = ((((a * i) + b) - d) / c)
	    if ((j == int(j)) and (j >= 0)):
	        global_list.append(((a * i) + b))
	        break
	else:
	    global_list.append((- 1))
	return global_list