def func(*args):
	
	(n, k) = args[0].strip().split(' ')
	(n, k) = [int(n), int(k)]
	i = 0
	sum1 = 0
	while (i <= n):
	    sum1 += (5 * i)
	    if ((sum1 + k) > 240):
	        break
	    i += 1
	return((i - 1))
