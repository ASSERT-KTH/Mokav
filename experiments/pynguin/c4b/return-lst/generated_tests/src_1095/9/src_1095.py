def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n < 3):
	    ret_values.append((- 1))
	    exit()
	cur = (10 ** (n - 1))
	ans = (((2 * 3) * 5) * 7)
	nex = (cur // ans)
	ret_values.append((ans * (nex + 1)))

	return ret_values
