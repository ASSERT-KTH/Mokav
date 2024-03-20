def func(*args):
	
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
	return(count)
