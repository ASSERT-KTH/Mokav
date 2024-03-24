def func(*args):
	ret_values = []
	
	import math
	(houses, goal) = map(int, args[0].split())
	if ((goal % 2) == 0):
	    ret_values.append((((houses - goal) // 2) + 1))
	else:
	    ret_values.append(math.ceil((goal / 2)))

	return ret_values
