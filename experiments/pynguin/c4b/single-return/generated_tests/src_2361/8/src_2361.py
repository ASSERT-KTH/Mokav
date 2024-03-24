def func(*args):
	
	(n, a, b, c) = map(int, args[0].split())
	res = ([float('-inf')] * 5000)
	res[0] = 0
	for i in range(1, (n + 1)):
	    res[i] = (1 + max(res[(i - a)], res[(i - b)], res[(i - c)]))
	return(res[n])
