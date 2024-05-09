def original_func(*args):
	global_list = []
	
	import math
	(a, b) = map(int, args[0].split())
	ans = 0
	cnt = 0
	need = 1
	while True:
	    a = max(a, 0)
	    b = max(b, 0)
	    if (a == 0):
	        global_list.append('Valera')
	        break
	    if (b == 0):
	        global_list.append('Vladik')
	        break
	    if ((cnt % 2) == 0):
	        a -= need
	    else:
	        b -= need
	    need += 1
	    cnt += 1
	return global_list