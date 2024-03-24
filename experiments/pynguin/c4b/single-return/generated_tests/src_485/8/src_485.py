def func(*args):
	
	(a, b) = (int(i) for i in args[0].split())
	return(('YES' if ((abs((a - b)) <= 1) and ((a + b) > 0)) else 'NO'))
