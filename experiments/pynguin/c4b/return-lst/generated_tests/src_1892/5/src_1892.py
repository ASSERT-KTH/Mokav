def func(*args):
	ret_values = []
	
	import math
	import re
	a = args[0]
	if ((a == 'a1') or (a == 'h1') or (a == 'a8') or (a == 'h8')):
	    ret_values.append(3)
	elif ((a[1] == '1') or (a[1] == '8') or (a[0] == 'a') or (a[0] == 'h')):
	    ret_values.append(5)
	else:
	    ret_values.append(8)

	return ret_values
