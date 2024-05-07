def original_func(*args):
	global_list = []
	
	from math import inf
	(m, b) = map(int, args[0].split())
	ans = (- inf)
	for y in range(b):
	    x = ((b - y) * m)
	    x = int(x)
	    if (ans < (((((x + 1) * y) * (y + 1)) / 2) + ((((y + 1) * x) * (x + 1)) / 2))):
	        ans = (((((x + 1) * y) * (y + 1)) / 2) + ((((y + 1) * x) * (x + 1)) / 2))
	global_list.append(int(ans))
	return global_list