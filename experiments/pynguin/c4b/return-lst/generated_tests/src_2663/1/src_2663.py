def func(*args):
	ret_values = []
	
	(s, r) = list(map(int, args[0].split()))
	if (s > r):
	    temp = (s // 2)
	    dip = (temp // (r + 1))
	    cert = (r * dip)
	    ret_values.append('{} {} {}'.format(dip, cert, ((s - dip) - cert)))
	else:
	    ret_values.append('{} {} {}'.format('0', '0', s))

	return ret_values
