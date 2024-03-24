def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (n, k) = map(int, args[0].split())
	    line = [str((it + 1)) for it in range(n)]
	    line = ([str(it) for it in range(n, (n - k), (- 1))] + [str(it) for it in range(1, ((n - k) + 1))])
	    ret_values.append(' '.join(line))

	return ret_values
