def func(*args):
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	sum1 = v0
	days = 1
	while (sum1 < c):
	    sum1 += min(((v0 + (days * a)) - l), (v1 - l))
	    days += 1
	return(days)
