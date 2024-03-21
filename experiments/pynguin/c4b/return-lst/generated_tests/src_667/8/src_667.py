def func(*args):
	ret_values = []
	
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
	ret_values.append(len(result))

	return ret_values
