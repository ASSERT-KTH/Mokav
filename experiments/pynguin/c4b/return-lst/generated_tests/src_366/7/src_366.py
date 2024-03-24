def func(*args):
	ret_values = []
	
	a = args[0]
	b = a.split()
	b.sort(key=float)
	dist = 200
	xn = int(b[0])
	while (xn <= int(b[2])):
	    if (((abs((xn - int(b[0]))) + abs((xn - int(b[1])))) + abs((xn - int(b[2])))) < dist):
	        dist = ((abs((xn - int(b[0]))) + abs((xn - int(b[1])))) + abs((xn - int(b[2]))))
	    xn += 1
	ret_values.append(dist)

	return ret_values
