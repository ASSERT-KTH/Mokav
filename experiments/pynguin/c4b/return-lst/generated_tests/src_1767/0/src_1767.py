def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n < 13):
	    ret_values.append(pow(2, n))
	else:
	    num = pow(2, 12)
	    n = (n - 13)
	    ans = 8092
	    while n:
	        ans = (ans * 2)
	        n = (n - 1)
	    ret_values.append(ans)

	return ret_values
