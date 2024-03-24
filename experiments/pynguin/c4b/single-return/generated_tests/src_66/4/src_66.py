def func(*args):
	
	l = [int(x) for x in args[0].split()]
	ans = 0
	d = []
	for e in l:
	    if (e in d):
	        ans += 1
	    else:
	        d.append(e)
	return(ans)
