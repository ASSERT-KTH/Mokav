def original_func(*args):
	global_list = []
	
	n = int(args[0])
	b = 0
	for i in range(1, n):
	    if (((n % i) == 0) and (i != 0)):
	        a = i
	        if ((float((a ** (1 / 2))) == int((a ** (1 / 2)))) and (a != 1)):
	            b = (b + 1)
	if (b == 0):
	    global_list.append(n)
	else:
	    global_list.append(a)
	return global_list