def func(*args):
	ret_values = []
	
	(n, s) = map(int, args[0].split())
	counter = 0
	if (n >= s):
	    for d in range(s, (n + 1)):
	        c = 0
	        f = d
	        while (d != 0):
	            e = (d % 10)
	            c = (c + e)
	            d = int((d // 10))
	        check = (f - c)
	        if (check < s):
	            counter = (counter + 1)
	        else:
	            break
	    x = (((n + 1) - counter) - s)
	    ret_values.append(x)
	else:
	    x = 0
	    ret_values.append(x)

	return ret_values
