def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	(c, b, a) = sorted([a, b, c])
	ret_values.append(max(((((i // a) + (j // b)) + (((n - i) - j) // c)) for i in range(0, (min(n, (b * a)) + 1), a) for j in range(0, (min(n, (c * b)) + 1), b) if ((((n - i) - j) % c) == 0))))

	return ret_values
