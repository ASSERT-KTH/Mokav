def func(*args):
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	S = ((k * l) // nl)
	S1 = (c * d)
	S2 = (p // np)
	return((min(S, S1, S2) // n))
