def func(*args):
	
	'input\n2 3 4\n'
	(a, b, c) = sorted(map(int, args[0].split()))
	return(((((b + a) - 1) * ((c + a) - 1)) - (a * (a - 1))))
