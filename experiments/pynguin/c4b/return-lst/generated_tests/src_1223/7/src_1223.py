def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	ans = min((n - a), (b + 1))
	ret_values.append(ans)

	return ret_values
