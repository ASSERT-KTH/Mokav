def func(*args):
	ret_values = []
	
	from math import log
	n = int(args[0])
	m = int(args[1])
	imp = (- 1)
	i = 0
	while ((m >= n) and ((m % n) == 0)):
	    m /= n
	    i += 1
	if (m == 1):
	    imp = i
	if (imp != (- 1)):
	    ret_values.append('YES')
	    ret_values.append((int(imp) - 1))
	else:
	    ret_values.append('NO')

	return ret_values
