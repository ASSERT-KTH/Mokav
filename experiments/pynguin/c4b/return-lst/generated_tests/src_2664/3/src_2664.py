def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	diploma = ((n // 2) // (k + 1))
	gram = (diploma * k)
	s = ((n - gram) - diploma)
	ret_values.append(diploma, gram, s)

	return ret_values
