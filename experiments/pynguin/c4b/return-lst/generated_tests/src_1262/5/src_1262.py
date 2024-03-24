def func(*args):
	ret_values = []
	
	(a, b, ab) = map(int, args[0].split())
	ret_values.append(min(((a + b) + ab), ((2 * a) + (2 * b)), ((2 * a) + (2 * ab)), ((2 * b) + (2 * ab))))

	return ret_values
