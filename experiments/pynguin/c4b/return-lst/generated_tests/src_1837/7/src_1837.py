def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	ans = ((a // k) + (b // k))
	if (((a < k) and (b % k)) or ((b < k) and (a % k))):
	    ans = (- 1)
	ret_values.append(ans)

	return ret_values
