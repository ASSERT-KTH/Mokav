def func(*args):
	
	(a, b) = map(int, args[0].split())
	n = int((a ** 0.5))
	return(('Vladik' if ((n * (n + 1)) <= b) else 'Valera'))
