def func(*args):
	ret_values = []
	
	a = int(args[0])
	l = []
	b = l.extend(map(int, args[1].split()))
	l.sort()
	l.reverse()
	sum = 0
	count = 0
	i = 0
	while (sum < a):
	    sum += l[i]
	    i += 1
	    count += 1
	    if ((count == 12) and (sum < a)):
	        ret_values.append((- 1))
	        exit()
	ret_values.append(count)

	return ret_values
