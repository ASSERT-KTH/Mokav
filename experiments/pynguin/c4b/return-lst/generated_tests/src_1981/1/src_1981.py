def func(*args):
	ret_values = []
	
	a = args[0].split()
	y = int(a[0])
	k = int(a[1])
	n = int(a[2])
	xl = []
	xf = (- 1)
	div = (n // k)
	mul = (div * k)
	xmax = (mul - y)
	if (xmax < 1):
	    ret_values.append((- 1))
	else:
	    xl.append(xmax)
	    while True:
	        xmax -= k
	        if (xmax < 1):
	            break
	        xl.append(xmax)
	    xl.sort()
	    ans = ''
	    for k in xl:
	        ans += (str(k) + ' ')
	    ret_values.append(ans)

	return ret_values
