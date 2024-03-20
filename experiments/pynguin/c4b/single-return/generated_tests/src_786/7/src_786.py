def func(*args):
	
	n = int(args[0])
	ans = ''
	for i in range(32, (- 1), (- 1)):
	    if ((n & (1 << i)) is not 0):
	        ans += str((i + 1))
	        ans += ' '
	return(ans)
