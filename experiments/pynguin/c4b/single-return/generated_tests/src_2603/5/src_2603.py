def func(*args):
	
	ans = 0
	rawInp = args[0].split(' ')
	(a, b) = (int(rawInp[0]), int(rawInp[1]))
	while (a <= b):
	    a *= 3
	    b *= 2
	    ans += 1
	return(ans)
