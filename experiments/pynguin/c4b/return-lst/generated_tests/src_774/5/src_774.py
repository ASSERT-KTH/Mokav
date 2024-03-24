def func(*args):
	ret_values = []
	
	(m, d) = map(int, args[0].split())
	if (m == 2):
	    ans = (4 + [0, 1][(d != 1)])
	elif (m in [4, 6, 9, 11]):
	    ans = (5 + [0, 1][(d > 6)])
	else:
	    ans = (5 + [0, 1][(d > 5)])
	ret_values.append(ans)

	return ret_values
