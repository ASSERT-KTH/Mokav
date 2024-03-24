def func(*args):
	ret_values = []
	
	import math
	nbr = int(args[0])
	s = int(math.sqrt((2 * nbr)))
	if ((nbr == ((s * (s + 1)) / 2)) or (nbr == (((s + 1) * (s + 2)) / 2))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
