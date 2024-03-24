def func(*args):
	ret_values = []
	
	k = int(args[0])
	b = args[1].split()
	a = []
	for i in b:
	    a.append(int(i))
	sum = 0
	for i in a:
	    sum += i
	if (k > sum):
	    ret_values.append('-1')
	else:
	    count = 0
	    while (k > 0):
	        k -= max(a)
	        a.remove(max(a))
	        count += 1
	    ret_values.append(count)

	return ret_values
