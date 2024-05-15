def patched_func(*args):
	global_list = []
	
	(k, a, b) = [int(i) for i in args[0].split()]
	resa = (a // k)
	resb = (b // k)
	osta = (a % k)
	ostb = (b % k)
	res = (resa + resb)
	if ((res == 0) or ((resa == 0) and (ostb != 0)) or ((resb == 0) and (osta != 0))):
	    global_list.append((- 1))
	else:
	    global_list.append(res)
	return global_list