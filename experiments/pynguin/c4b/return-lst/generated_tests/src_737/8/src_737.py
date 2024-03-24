def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	count = 0
	for ci in range((c + 1)):
	    x = (n - (2 * ci))
	    if (x < 0):
	        break
	    high = min(b, x)
	    low = max(0, (x - (a // 2)))
	    if (high >= low):
	        count += ((high - low) + 1)
	ret_values.append(count)

	return ret_values
