def func(*args):
	
	a = list(map(int, args[0].split()))
	a.sort()
	afstand = (abs((a[0] - a[1])) + abs((a[2] - a[1])))
	return(afstand)
