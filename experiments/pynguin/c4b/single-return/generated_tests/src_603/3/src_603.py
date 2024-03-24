def func(*args):
	
	(a, b) = map(int, args[0].split())
	return(('YES' if ((abs((a - b)) <= 1) and (max(a, b) > 0)) else 'NO'))
