def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	for l in range(1, 3):
	    for r in range(l, 555):
	        (o, e) = (0, 0)
	        for x in range(l, (r + 1)):
	            o += (x % 2)
	            e += (1 - (x % 2))
	        if ((o == b) and (e == a)):
	            ret_values.append('YES')
	            exit()
	ret_values.append('NO')

	return ret_values
