def func(*args):
	
	(n, a, b, c, d) = map(int, args[0].split())
	min_a11 = max(1, ((1 + c) - b))
	max_a11 = min(n, ((n + c) - b))
	min_a11 = max(min_a11, ((1 + d) - a))
	max_a11 = min(max_a11, ((n + d) - a))
	min_a11 = max(min_a11, ((((1 + c) + d) - a) - b))
	max_a11 = min(max_a11, ((((n + c) + d) - a) - b))
	return((n * max(((max_a11 - min_a11) + 1), 0)))
