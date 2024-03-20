def func(*args):
	
	n = int(args[0])
	a = ((2 ** (len(str(n)) - 1)) - 1)
	i = 0
	while (int(bin(((2 ** (len(str(n)) - 1)) + i)).replace('b', '0')) <= n):
	    i += 1
	return((a + i))
