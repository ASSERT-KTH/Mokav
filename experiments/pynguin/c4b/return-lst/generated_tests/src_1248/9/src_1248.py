def func(*args):
	ret_values = []
	
	(n, m) = args[0].split()
	n = int(n)
	m = int(m)
	l = ((n - 1) - m)
	if ((m >= n) or ((l * (l + 1)) < (2 * (n - m)))):
	    m = n
	    ret_values.append(n)
	else:
	    a = (2 * (n - m))
	    u = 1
	    l = ((n - 1) - m)
	    while (u != l):
	        mid = ((u + l) // 2)
	        if ((mid * (mid + 1)) >= a):
	            if (((mid - 1) * mid) < a):
	                break
	            else:
	                l = (mid - 1)
	        elif (((mid + 1) * (mid + 2)) >= a):
	            mid += 1
	            break
	        else:
	            u = (mid + 1)
	    ret_values.append((mid + m))

	return ret_values
