def func(*args):
	ret_values = []
	
	import sys
	stdin = sys.stdin.read().splitlines()
	(n, k) = map(int, stdin[0].split())
	x = ((int((((8 * ((240 - k) // 5)) + 1) ** (1 / 2.0))) - 1) / 2)
	if (x > n):
	    ret_values.append(n)
	else:
	    ret_values.append(int(x))

	return ret_values
