def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	punched = ([False] * d)
	for i in range(d):
	    if (((i - 1) % k) == 0):
	        punched[i] = True
	    if (((i - 1) % l) == 0):
	        punched[i] = True
	    if (((i - 1) % m) == 0):
	        punched[i] = True
	    if (((i - 1) % n) == 0):
	        punched[i] = True
	sum = 0
	for r in range(d):
	    if (punched[(r - 1)] == True):
	        sum += 1
	global_list.append(sum)
	return global_list