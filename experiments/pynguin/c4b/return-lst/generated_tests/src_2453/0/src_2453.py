def func(*args):
	ret_values = []
	
	n = int(args[0])
	week = list(map(int, args[1].split()))
	s = 0
	i = 0
	while (s < n):
	    s = (s + week[i])
	    if (i == 6):
	        i = 0
	    else:
	        i += 1
	if (i == 0):
	    ret_values.append(7)
	else:
	    ret_values.append(i)

	return ret_values
