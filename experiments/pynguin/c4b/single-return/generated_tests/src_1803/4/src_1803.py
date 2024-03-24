def func(*args):
	
	b = []
	a = str(args[0]).split()
	for i in range(4):
	    if (a[i] not in b):
	        b.append(a[i])
	return((4 - len(b)))
