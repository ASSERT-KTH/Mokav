def func(*args):
	
	n = int(args[0])
	a = int(args[1])
	b = int(args[2])
	c = int(args[3])
	ans = 0
	if ((a <= (b - c)) or (n < b)):
	    ans = (n // a)
	else:
	    ans = ((n - c) // (b - c))
	    rem = ((c + (n - c)) - ((b - c) * ans))
	    while (rem >= b):
	        rem = (rem - (b - c))
	        ans += 1
	    if (rem >= a):
	        ans += (rem // a)
	return(ans)
