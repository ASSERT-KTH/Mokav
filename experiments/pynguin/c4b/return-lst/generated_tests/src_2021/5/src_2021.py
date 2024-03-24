def func(*args):
	ret_values = []
	
	import math
	s = args[0]
	n = int(s.split()[0])
	m = int(s.split()[1])
	k = int(s.split()[2])
	i = math.ceil((k / (2 * m)))
	k -= (((i - 1) * 2) * m)
	j = math.ceil((k / 2))
	if ((k % 2) == 1):
	    ret_values.append(('%d %d L' % (i, j)))
	else:
	    ret_values.append(('%d %d R' % (i, j)))

	return ret_values
