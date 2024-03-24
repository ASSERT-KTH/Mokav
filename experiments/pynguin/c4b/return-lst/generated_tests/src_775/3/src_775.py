def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	ret_values.append(((- 1) if (((a < k) and (b < k)) or (((max(a, b) % k) > 0) and (min(a, b) < k))) else ((a // k) + (b // k))))

	return ret_values
