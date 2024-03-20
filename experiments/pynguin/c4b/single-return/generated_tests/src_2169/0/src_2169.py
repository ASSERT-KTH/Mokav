def func(*args):
	
	(a, b, c, d, e, f) = map(int, args[0].split())
	return(('Ron' if ((((a * e) * c) < ((f * d) * b)) or ((c == 0) and d) or ((a == 0) and b and d)) else 'Hermione'))
