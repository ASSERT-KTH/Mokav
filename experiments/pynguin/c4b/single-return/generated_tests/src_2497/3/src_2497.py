def func(*args):
	
	(n, a, b, c) = map(int, args[0].split())
	mem = ([0] * (n + 1))
	mem[n] = 1
	for i in range(n, (- 1), (- 1)):
	    if (mem[i] != 0):
	        if ((i - a) >= 0):
	            mem[(i - a)] = max(mem[(i - a)], (mem[i] + 1))
	        if ((i - b) >= 0):
	            mem[(i - b)] = max(mem[(i - b)], (mem[i] + 1))
	        if ((i - c) >= 0):
	            mem[(i - c)] = max(mem[(i - c)], (mem[i] + 1))
	return((mem[0] - 1))
