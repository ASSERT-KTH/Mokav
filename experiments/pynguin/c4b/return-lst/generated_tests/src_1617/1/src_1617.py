def func(*args):
	ret_values = []
	
	from math import log2
	(n, b, p) = map(int, args[0].split())
	(m, res_b) = (n, 0)
	while (m > 1):
	    in_match = (2 ** int(log2(m)))
	    go_through = int((m - in_match))
	    res_b += int(((b * in_match) + (in_match / 2)))
	    m = int(((in_match / 2) + go_through))
	ret_values.append(res_b, (p * n))

	return ret_values
