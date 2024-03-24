def func(*args):
	ret_values = []
	
	i = int(args[0])
	y = list()
	x = list()
	f = 1
	while ((y != x) or (f == 1)):
	    f = 0
	    i += 1
	    a = str(i)
	    x = list()
	    y = list()
	    for j in range(0, len(a)):
	        x.append(a[j])
	    y = sorted(set(x))
	    x = sorted(x)
	    if (y == x):
	        ret_values.append(i)
	        break

	return ret_values
