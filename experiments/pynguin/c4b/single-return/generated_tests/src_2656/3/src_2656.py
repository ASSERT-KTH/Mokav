def func(*args):
	
	(a, b) = map(int, args[0].split())
	i = 1
	while True:
	    a = (a - i)
	    if (a < 0):
	        ans = 'Vladik'
	        break
	    i += 1
	    b = (b - i)
	    if (b < 0):
	        ans = 'Valera'
	        break
	    i += 1
	return(ans)
