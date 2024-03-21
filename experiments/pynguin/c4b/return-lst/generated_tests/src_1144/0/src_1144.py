def func(*args):
	ret_values = []
	
	n = int(args[0])
	week = [int(x) for x in args[1].split()]
	s = sum(week)
	n %= s
	if n:
	    i = 0
	    while (n > week[i]):
	        n -= week[i]
	        i += 1
	    ret_values.append((i + 1))
	else:
	    i = 6
	    while ((not week[i]) and (i >= 0)):
	        i -= 1
	    ret_values.append((i + 1))

	return ret_values
