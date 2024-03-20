def func(*args):
	
	(m, n, a) = map(int, args[0].split())
	nvag = int((n / a))
	mvag = int((m / a))
	if ((n % a) != 0):
	    nvag += 1
	if ((m % a) != 0):
	    mvag += 1
	return((nvag * mvag))
