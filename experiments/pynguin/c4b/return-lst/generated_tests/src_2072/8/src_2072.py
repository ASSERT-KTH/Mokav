def func(*args):
	ret_values = []
	
	w = int(args[0])
	x = (w - 1)
	n = 0
	for i in range(1, ((w // 2) + 2)):
	    if (((i % 2) == 0) and ((x % 2) == 0)):
	        ret_values.append('YES')
	        n += 1
	        break
	    x -= 1
	    if (x == 0):
	        break
	if (n == 0):
	    ret_values.append('NO')

	return ret_values
