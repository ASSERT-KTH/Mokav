def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = list(map(int, args[1].split()))
	s.sort(reverse=True)
	(c, d, x) = (0, (- 1), 0)
	for i in range(12):
	    c = (c + 1)
	    x = (x + s[i])
	    if (x >= n):
	        d = 1
	        break
	if (n == 0):
	    ret_values.append(0)
	else:
	    ret_values.append((c if (d > 0) else (- 1)))

	return ret_values
