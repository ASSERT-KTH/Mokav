def func(*args):
	
	n = int(args[0])
	pairs = (n // 2)
	leftover = (n % 2)
	ans = [('aa' if ((x % 2) == 0) else 'bb') for x in range(pairs)]
	if leftover:
	    if (len(ans) > 0):
	        ans += (['b'] if (ans[(- 1)] == 'aa') else 'a')
	    else:
	        ans = ['a']
	return(''.join(ans))
