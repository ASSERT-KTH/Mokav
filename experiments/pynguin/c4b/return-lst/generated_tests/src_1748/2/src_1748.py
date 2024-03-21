def func(*args):
	ret_values = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	drink_toast = ((k * l) // nl)
	lime_toast = (c * d)
	salt_toast = (p // np)
	ret_values.append((min(drink_toast, lime_toast, salt_toast) // n))

	return ret_values
