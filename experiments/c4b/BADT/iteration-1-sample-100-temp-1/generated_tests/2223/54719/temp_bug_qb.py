def original_func(*args):
	global_list = []
	
	import math
	weight = int(args[0])
	w1 = math.ceil((weight / 2))
	w2 = (weight - w1)
	global_list.append(w1)
	global_list.append(w2)
	if (((weight % 2) == 0) or (((w1 % 2) == 0) and ((w2 % 2) == 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list