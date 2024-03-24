def func(*args):
	ret_values = []
	
	(n, a, b, c) = list(map(int, args[0].split()))
	f = ([(- 1)] * 5000)
	f[0] = 0
	for i in range(1, (n + 1)):
	    if ((i >= a) and (f[(i - a)] != (- 1))):
	        f[i] = max(f[i], (f[(i - a)] + 1))
	    if ((i >= b) and (f[(i - b)] != (- 1))):
	        f[i] = max(f[i], (f[(i - b)] + 1))
	    if ((i >= c) and (f[(i - c)] != (- 1))):
	        f[i] = max(f[i], (f[(i - c)] + 1))
	ret_values.append(f[n])

	return ret_values
