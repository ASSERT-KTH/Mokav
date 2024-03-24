def func(*args):
	
	import math
	(k, l) = [int(args[0]) for i in range(2)]
	i = math.floor((math.log(l, k) + 0.5))
	return(('NO' if (l != (k ** i)) else ('YES\n' + str((i - 1)))))
