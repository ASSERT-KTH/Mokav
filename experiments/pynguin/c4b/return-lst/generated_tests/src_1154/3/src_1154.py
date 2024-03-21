def func(*args):
	ret_values = []
	
	s = args[0].split()
	n = int(s[0])
	m = int(s[1])
	k = int(s[(- 1)])
	r = (((k + (2 * m)) - 1) // (2 * m))
	d = (k - ((r - 1) * (2 * m)))
	d = ((d + 1) // 2)
	ret_values.append(r, d, end=' ')
	if (k % 2):
	    ret_values.append('L')
	else:
	    ret_values.append('R')

	return ret_values
