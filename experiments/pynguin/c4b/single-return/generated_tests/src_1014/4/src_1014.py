def func(*args):
	
	n = int(args[0])
	l = args[1]
	l = [int(i) for i in l.split()]
	l = sorted(l)
	return(l[(len(l) // 2)])
