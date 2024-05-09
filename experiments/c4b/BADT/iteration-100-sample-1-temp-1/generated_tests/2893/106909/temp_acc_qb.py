def patched_func(*args):
	global_list = []
	
	(s, r) = list(map(int, args[0].split()))
	if (s > r):
	    temp = (s // 2)
	    dip = (temp // (r + 1))
	    cert = (r * dip)
	    global_list.append('{} {} {}'.format(dip, cert, ((s - dip) - cert)))
	else:
	    global_list.append('{} {} {}'.format('0', '0', s))
	return global_list