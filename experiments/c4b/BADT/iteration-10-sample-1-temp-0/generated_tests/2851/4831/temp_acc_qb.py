def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	cnt = 1
	while True:
	    if ((cnt % 2) == 1):
	        a -= cnt
	    else:
	        b -= cnt
	    if (b < 0):
	        global_list.append('Valera')
	        break
	    if (a < 0):
	        global_list.append('Vladik')
	        break
	    cnt += 1
	return global_list