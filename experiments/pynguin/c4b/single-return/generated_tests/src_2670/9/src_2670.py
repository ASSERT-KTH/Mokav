def func(*args):
	
	a = args[0]
	b = args[1].split('0')
	ans = ([0] * len(b))
	for i in range(len(b)):
	    ans[i] = str(len(b[i]))
	return(''.join(ans))
