def func(*args):
	
	(M, N) = map(int, args[0].split(' '))
	if (1 <= M <= N <= 16):
	    s = (M * N)
	    return((s // 2))
