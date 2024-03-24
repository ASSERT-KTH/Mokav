def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	an = list(map(int, sys.stdin.readline().split()))
	total = sum(an)
	m = (n % total)
	if ((m == 0) and (n != 0)):
	    n = total
	else:
	    n = m
	ans = 0
	while ((n > 0) and (ans < 7)):
	    n -= an[ans]
	    if (n > 0):
	        ans += 1
	ret_values.append((1 + ans))

	return ret_values
