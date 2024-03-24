def func(*args):
	ret_values = []
	
	dc = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	(m, d) = map(int, args[0].split())
	ret_values.append((((dc[m] + d) + 5) // 7))

	return ret_values
