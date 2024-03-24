def func(*args):
	ret_values = []
	
	from sys import stdin
	n = int(stdin.readline())
	ret_values.append((1 + ((3 * n) * (n + 1))))

	return ret_values
