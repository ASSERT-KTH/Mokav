def patched_func(*args):
	global_list = []
	
	import math
	import re
	a = args[0]
	if ((a == 'a1') or (a == 'h1') or (a == 'a8') or (a == 'h8')):
	    global_list.append(3)
	elif ((a[1] == '1') or (a[1] == '8') or (a[0] == 'a') or (a[0] == 'h')):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list