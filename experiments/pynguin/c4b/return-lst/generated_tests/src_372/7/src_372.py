def func(*args):
	ret_values = []
	
	a = args[0]
	b = a.split()
	c = []
	i = 1
	while (i < 4):
	    c.append(int(b[i]))
	    i += 1
	
	def filter(a):
	    a.sort()
	    b = [a[0]]
	    if ((a[1] % a[0]) != 0):
	        b.append(a[1])
	    if (((a[2] % a[0]) != 0) and ((a[2] % a[1]) != 0) and ((a[0] + a[1]) != a[2])):
	        b.append(a[2])
	    b.sort()
	    return b
	d = filter(c)
	max = 0
	n = int(b[0])
	if (len(d) == 3):
	    for x in range(0, ((n // d[0]) + 1)):
	        for y in range(0, (((n - (x * d[0])) // d[1]) + 1)):
	            if (((n - ((x * d[0]) + (y * d[1]))) % d[2]) == 0):
	                if (max < ((x + y) + ((n - ((x * d[0]) + (y * d[1]))) // d[2]))):
	                    max = ((x + y) + ((n - ((x * d[0]) + (y * d[1]))) // d[2]))
	if (len(d) == 2):
	    for x in range(0, ((n // d[0]) + 1)):
	        if (((n - (x * d[0])) % d[1]) == 0):
	            if (max < (x + ((n - (x * d[0])) // d[1]))):
	                max = (x + ((n - (x * d[0])) // d[1]))
	if (len(d) == 1):
	    max = (n // d[0])
	ret_values.append(max)

	return ret_values
