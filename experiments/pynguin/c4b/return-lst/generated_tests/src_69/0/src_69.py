def func(*args):
	ret_values = []
	
	a = [int(i) for i in args[0].split()]
	t = 0
	if (a == [1, 1]):
	    ret_values.append(0)
	else:
	    while ((a[0] > 0) and (a[1] > 0)):
	        if (a[1] > a[0]):
	            a[0] += 1
	            a[1] -= 2
	        else:
	            a[0] -= 2
	            a[1] += 1
	        t += 1
	    ret_values.append(t)

	return ret_values
