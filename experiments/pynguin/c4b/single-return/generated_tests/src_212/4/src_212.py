def func(*args):
	
	l = sorted(list(map(int, args[0].split())))
	p = l[(len(l) // 2)]
	sh = 0
	for i in l:
	    sh += abs((i - p))
	return(sh)
