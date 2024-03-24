def func(*args):
	
	n = int(args[0])
	(kid, count, res) = (1, 1, [])
	for i in range((n - 1)):
	    kid = ((kid + count) % n)
	    res.append((n if (kid == 0) else kid))
	    count += 1
	return(*res)
