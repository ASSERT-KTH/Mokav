def func(*args):
	
	n = args[0]
	l = len(n)
	b = ''
	for i in range(l):
	    a = int(n[i])
	    if (a == 0):
	        b += '0'
	    elif (a == 1):
	        b += '1'
	    elif (a > 1):
	        b += ('1' * (l - i))
	        break
	ans = 0
	for i in range(l):
	    ans += (int(b[((l - 1) - i)]) * (2 ** i))
	return(ans)
