def func(*args):
	
	(k, a, b) = map(int, args[0].split())
	return(((- 1) if (((a < k) and (b < k)) or (((max(a, b) % k) > 0) and (min(a, b) < k))) else ((a // k) + (b // k))))
