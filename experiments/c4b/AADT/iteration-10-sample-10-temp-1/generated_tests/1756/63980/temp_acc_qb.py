def patched_func(*args):
	global_list = []
	
	a = args[0].split()
	answ = 0
	ban = []
	for (i, x) in enumerate(a):
	    if ((a.count(x) != 1) and (x not in ban)):
	        answ += (a.count(x) - 1)
	        ban.append(x)
	global_list.append(answ)
	return global_list