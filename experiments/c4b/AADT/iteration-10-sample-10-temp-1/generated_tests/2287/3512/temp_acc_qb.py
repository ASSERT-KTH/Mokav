def patched_func(*args):
	global_list = []
	
	import math
	(a, b) = args[0].split()
	digits = list((str(a) + str(b)))
	base = (int(max(digits)) + 1)
	a = int(str(a), base)
	b = int(str(b), base)
	sumResult = (a + b)
	start = 1
	result = ''
	while (sumResult > 0):
	    mod = (sumResult % base)
	    result += str(mod)
	    sumResult = math.floor((sumResult / base))
	global_list.append(len(result))
	return global_list