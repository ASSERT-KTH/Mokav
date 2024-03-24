def func(*args):
	ret_values = []
	
	p = args[0]
	p.split()
	y = [int(i) for i in p]
	m = y[0]
	count = 1
	a = len(y)
	x = (- 1)
	for i in range(1, a):
	    if (y[i] == m):
	        count = (count + 1)
	        if (count == 7):
	            x = 0
	            break
	    else:
	        m = y[i]
	        count = 1
	if (x == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
