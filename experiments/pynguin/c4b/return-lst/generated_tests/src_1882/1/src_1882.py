def func(*args):
	ret_values = []
	
	(a, b, c) = args[0].split()
	(prvni, interval, jist) = [int(a), int(b), int(c)]
	if ((jist >= prvni) and (jist != (prvni + 1)) and ((((jist - prvni) % interval) == 0) or ((((jist - prvni) - 1) % interval) == 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
