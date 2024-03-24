def func(*args):
	ret_values = []
	
	(x1, y1) = map(int, args[0].split())
	(x2, y2) = map(int, args[1].split())
	ret_values.append(max(abs((x2 - x1)), abs((y2 - y1))))

	return ret_values
