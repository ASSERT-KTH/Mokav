def func(*args):
	ret_values = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	S = ((k * l) // nl)
	S1 = (c * d)
	S2 = (p // np)
	ret_values.append((min(S, S1, S2) // n))

	return ret_values
