def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	x = 1
	while (0 != ((a * x) % 10) != b):
	    x = (x + 1)
	ret_values.append(x)

	return ret_values
