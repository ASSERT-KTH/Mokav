def func(*args):
	
	a = args[0]
	return((a.upper() if ((sum((a.count(x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')) * 2) > len(a)) else a.lower()))
