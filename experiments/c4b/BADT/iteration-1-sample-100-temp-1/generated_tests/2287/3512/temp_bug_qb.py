def original_func(*args):
	global_list = []
	
	import math
	(a, b) = args[0].split()
	sumResult = (int(a) + int(b))
	digits = list((str(a) + str(b)))
	base = (int(max(digits)) + 1)
	start = 1
	result = ''
	while (sumResult > 0):
	    mod = (sumResult % base)
	    result += str(mod)
	    sumResult = math.floor((sumResult / base))
	global_list.append(len(result))
	return global_list