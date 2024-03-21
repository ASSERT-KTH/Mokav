def func(*args):
	ret_values = []
	
	(n, a, b) = list(map(int, args[0].split()))
	ans = ((n - max((a + 1), (n - b))) + 1)
	ret_values.append(ans)

	return ret_values
