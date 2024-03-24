def func(*args):
	ret_values = []
	
	import math
	(k, l) = [int(args[0]) for i in range(2)]
	i = math.floor((math.log(l, k) + 0.5))
	ret_values.append(('NO' if (l != (k ** i)) else ('YES\n' + str((i - 1)))))

	return ret_values
