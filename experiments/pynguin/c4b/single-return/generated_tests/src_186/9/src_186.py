def func(*args):
	
	import math
	(v1, v2, v3) = map(int, args[0].split())
	return(int((4 * ((math.sqrt(((v1 * v2) / v3)) + math.sqrt(((v2 * v3) / v1))) + math.sqrt(((v1 * v3) / v2))))))
