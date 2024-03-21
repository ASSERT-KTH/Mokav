def func(*args):
	ret_values = []
	
	import math
	(v1, v2, v3) = map(int, args[0].split())
	ret_values.append(int((4 * ((math.sqrt(((v1 * v2) / v3)) + math.sqrt(((v2 * v3) / v1))) + math.sqrt(((v1 * v3) / v2))))))

	return ret_values
