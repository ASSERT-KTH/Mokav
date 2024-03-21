def func(*args):
	ret_values = []
	
	from math import *
	k = int(args[0])
	l = int(args[1])
	x = (log(l) / log(k))
	xx = round(x)
	ret_values.append((('YES\n%d' % (xx - 1)) if (abs((x - xx)) < 1e-12) else 'NO'))

	return ret_values
