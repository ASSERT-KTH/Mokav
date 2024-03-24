def func(*args):
	ret_values = []
	
	x = int(args[0])
	(a, b, c, d, e, f, g, h, i, j, k, l) = map(int, args[1].split())
	lst = [a, b, c, d, e, f, g, h, i, j, k, l]
	lst.sort(reverse=True)
	z = 0
	if (x == 0):
	    ret_values.append('0')
	else:
	    for i in range(len(lst)):
	        z += lst[i]
	        if (z >= x):
	            a = (i + 1)
	            break
	        else:
	            a = (- 1)
	    ret_values.append(a)

	return ret_values
