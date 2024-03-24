def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split(' '))
	y = (a + b)
	while 1:
	    if (b == 0):
	        ret_values.append(a)
	        break
	    elif (y <= 0):
	        y += n
	    elif (y > n):
	        y -= n
	    else:
	        ret_values.append(y)
	        break

	return ret_values
