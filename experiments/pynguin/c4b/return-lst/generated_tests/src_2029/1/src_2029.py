def func(*args):
	ret_values = []
	
	(n, t, k, d) = list(map(int, args[0].strip().split(' ')))
	old = 0
	total = 0
	time1 = 0
	while (total < n):
	    if (((time1 % t) == 0) and (time1 > 0)):
	        total += k
	    time1 += 1
	old = time1
	total = 0
	time1 = 0
	time2 = 0
	check = 0
	while (total < n):
	    if (((time1 % t) == 0) and (time1 > 0)):
	        total += k
	        if ((time1 > d) and (check == 0)):
	            check = 1
	            start = time1
	    if ((check == 1) and (((time2 - start) % t) == 0)):
	        total += k
	    time1 += 1
	    time2 += 1
	if (time1 < old):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
