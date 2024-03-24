def func(*args):
	
	n = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort()
	if (n % 2):
	    return(a[(n // 2)])
