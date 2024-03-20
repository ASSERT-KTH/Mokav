def func(*args):
	
	n = int(args[0])
	k = args[1].split(' ')
	l = []
	for _ in k:
	    l.append(int(_))
	l = sorted(l)
	return(l[int((len(l) / 2))])
